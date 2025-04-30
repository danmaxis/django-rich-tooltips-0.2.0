# Uso Básico

O plugin funciona procurando por elementos HTML com atributos `data-` específicos e anexando o comportamento de tooltip a eles.

*   `data-tooltip-html="<p>Seu conteúdo <b>HTML</b> aqui</p>"`: Use para conteúdo HTML bruto. O conteúdo será **escapado** antes de ser colocado no atributo e, em seguida, decodificado pelo JavaScript antes da renderização.
*   `data-tooltip-markdown="# Seu Markdown\n\n*   Item de lista"`: Use para conteúdo Markdown. O conteúdo será **escapado** antes de ser colocado no atributo, decodificado pelo JavaScript e, em seguida, processado pelo `marked.js`.

**Importante:** Ao adicionar conteúdo dinâmico (HTML ou Markdown) a esses atributos em Python (por exemplo, em `admin.py`), sempre use `django.utils.html.escape()` no conteúdo antes de passá-lo para `format_html` para o valor do atributo. A parte JavaScript do plugin é projetada para lidar com esse conteúdo escapado.

### Exemplo: Adicionando Tooltips em `admin.py`

Você pode modificar os métodos `list_display` ou os widgets/textos de ajuda dos campos de formulário dentro do seu `ModelAdmin` para incluir esses atributos. Isso funciona tanto nas views de adição quanto nas de alteração.

```python
# models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    config_notes = models.TextField(
        blank=True,
        help_text="Insira os detalhes de configuração aqui."
    )

    # Exemplo: Armazenar conteúdo específico do tooltip no modelo
    details_tooltip_md = "## Campo Detalhes\n\nEste campo aceita texto *multilinha* descrevendo o item."
    html_tooltip_content = "<p>Este é um conteúdo <strong>HTML</strong> armazenado no modelo.</p>"

    def get_dynamic_tooltip(self):
        return f"Tooltip dinâmico baseado no nome: {self.name}"

# admin.py
from django.contrib import admin
from django.utils.html import format_html, escape
from .models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = (
        "name_with_dynamic_tooltip",
        "details_summary_with_markdown_tooltip",
        "config_notes_summary_with_html_tooltip",
    )

    # --- Tooltips na Listagem (List Display) ---

    # Exemplo 1: Tooltip de um método (texto simples)
    def name_with_dynamic_tooltip(self, obj):
        display_value = escape(obj.name)
        tooltip_value = obj.get_dynamic_tooltip() # Obtém texto dinâmico do método
        if tooltip_value:
            return format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(tooltip_value), # Escapa texto simples
                display_value
            )
        return display_value
    name_with_dynamic_tooltip.short_description = "Nome (Dica Dinâmica)"
    name_with_dynamic_tooltip.admin_order_field = "name"

    # Exemplo 2: Tooltip Markdown de um campo do modelo
    def details_summary_with_markdown_tooltip(self, obj):
        summary = escape(obj.details[:50] + '...' if len(obj.details) > 50 else obj.details)
        tooltip_value = getattr(obj, 'details_tooltip_md', None) # Markdown bruto
        if tooltip_value:
            return format_html(
                '<span data-tooltip-markdown="{}">{}</span>',
                escape(tooltip_value), # Escapa Markdown bruto
                summary
            )
        return summary
    details_summary_with_markdown_tooltip.short_description = "Detalhes (Dica MD)"

    # Exemplo 3: Tooltip HTML de um campo do modelo
    def config_notes_summary_with_html_tooltip(self, obj):
        summary = escape(obj.config_notes[:50] + '...' if len(obj.config_notes) > 50 else obj.config_notes)
        tooltip_value = getattr(obj, 'html_tooltip_content', None) # HTML bruto
        if tooltip_value:
            return format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(tooltip_value), # Escapa HTML bruto
                summary
            )
        return summary
    config_notes_summary_with_html_tooltip.short_description = "Config (Dica HTML)"


    # --- Tooltips no Formulário --- 
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # Adiciona tooltip HTML ao texto de ajuda do campo 'name' (funciona na adição/alteração)
        if 'name' in form.base_fields:
            name_tooltip = "Insira o nome <strong>único</strong> para este item."
            current_help = form.base_fields['name'].help_text or ''
            form.base_fields['name'].help_text = format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(name_tooltip), # Escapa HTML simples
                current_help
            )

        # Adiciona tooltip Markdown ao widget do campo 'details'
        if 'details' in form.base_fields:
            md_content = ""
            md_attr = "data-tooltip-html" # Padrão para HTML para ajuda genérica
            if obj and hasattr(obj, 'details_tooltip_md'): # Usa conteúdo específico do modelo na view de alteração
                md_content = obj.details_tooltip_md
                md_attr = "data-tooltip-markdown"
            else: # Ajuda genérica na view de adição
                md_content = 'Insira a descrição detalhada. Markdown é suportado para o tooltip na view de alteração.'
            form.base_fields['details'].widget.attrs.update({
                md_attr: escape(md_content)
            })

        # Adiciona um tooltip HTML estático ao widget do campo 'config_notes' (funciona na adição/alteração)
        if 'config_notes' in form.base_fields:
            config_tooltip = "<ul><li>Nota 1: Use formato JSON.</li><li>Nota 2: Reinicialização necessária após alteração.</li></ul>"
            form.base_fields['config_notes'].widget.attrs.update({
                'data-tooltip-html': escape(config_tooltip)
            })

        return form

```

### Exemplo: Adicionando Tooltips em Templates

Você pode adicionar os atributos `data-` diretamente a qualquer elemento HTML em seus templates Django (incluindo sobrescritas de templates do admin).

```html
{# Em algum_template.html #}

<label for="id_my_field">Meu Campo</label>
{# Lembre-se de escapar o conteúdo se for dinâmico ou contiver caracteres HTML especiais #}
{% with tooltip_content="Informação extra sobre <strong>Meu Campo</strong>." %}
<span data-tooltip-html="{{ tooltip_content|escape }}">?</span>
{% endwith %}
<input type="text" id="id_my_field" name="my_field">

{# Exemplo Markdown #}
{% with md_tooltip="## Ajuda da Seção\n\nEsta seção contém configurações relacionadas a X e Y." %}
<div data-tooltip-markdown="{{ md_tooltip|escape }}">
  <h2>Seção Importante</h2>
  <p>Algum conteúdo...</p>
</div>
{% endwith %}
```

