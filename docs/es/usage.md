# Uso Básico

El plugin funciona buscando elementos HTML con atributos `data-` específicos y adjuntando el comportamiento de tooltip a ellos.

*   `data-tooltip-html="<p>Tu contenido <b>HTML</b> aquí</p>"`: Úsalo para contenido HTML crudo. El contenido será **escapado** antes de ser colocado en el atributo, y luego decodificado por JavaScript antes de renderizar.
*   `data-tooltip-markdown="# Tu Markdown\n\n*   Elemento de lista"`: Úsalo para contenido Markdown. El contenido será **escapado** antes de ser colocado en el atributo, decodificado por JavaScript, y luego procesado por `marked.js`.

**Importante:** Al añadir contenido dinámico (HTML o Markdown) a estos atributos en Python (p. ej., en `admin.py`), siempre usa `django.utils.html.escape()` sobre el contenido antes de pasarlo a `format_html` para el valor del atributo. La parte JavaScript del plugin está diseñada para manejar este contenido escapado.

### Ejemplo: Añadiendo Tooltips en `admin.py`

Puedes modificar los métodos `list_display` o los widgets/textos de ayuda de los campos de formulario dentro de tu `ModelAdmin` para incluir estos atributos. Esto funciona tanto en las vistas de añadir como en las de modificar.

```python
# models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    config_notes = models.TextField(
        blank=True,
        help_text="Introduce los detalles de configuración aquí."
    )

    # Ejemplo: Almacenar contenido específico del tooltip en el modelo
    details_tooltip_md = "## Campo Detalles\n\nEste campo acepta texto *multilínea* describiendo el ítem."
    html_tooltip_content = "<p>Este es contenido <strong>HTML</strong> almacenado en el modelo.</p>"

    def get_dynamic_tooltip(self):
        return f"Tooltip dinámico basado en el nombre: {self.name}"

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

    # --- Tooltips en la Vista de Lista (List Display) ---

    # Ejemplo 1: Tooltip desde un método (texto simple)
    def name_with_dynamic_tooltip(self, obj):
        display_value = escape(obj.name)
        tooltip_value = obj.get_dynamic_tooltip() # Obtiene texto dinámico del método
        if tooltip_value:
            return format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(tooltip_value), # Escapa texto simple
                display_value
            )
        return display_value
    name_with_dynamic_tooltip.short_description = "Nombre (Tip Dinámico)"
    name_with_dynamic_tooltip.admin_order_field = "name"

    # Ejemplo 2: Tooltip Markdown desde un campo del modelo
    def details_summary_with_markdown_tooltip(self, obj):
        summary = escape(obj.details[:50] + '...' if len(obj.details) > 50 else obj.details)
        tooltip_value = getattr(obj, 'details_tooltip_md', None) # Markdown crudo
        if tooltip_value:
            return format_html(
                '<span data-tooltip-markdown="{}">{}</span>',
                escape(tooltip_value), # Escapa Markdown crudo
                summary
            )
        return summary
    details_summary_with_markdown_tooltip.short_description = "Detalles (Tip MD)"

    # Ejemplo 3: Tooltip HTML desde un campo del modelo
    def config_notes_summary_with_html_tooltip(self, obj):
        summary = escape(obj.config_notes[:50] + '...' if len(obj.config_notes) > 50 else obj.config_notes)
        tooltip_value = getattr(obj, 'html_tooltip_content', None) # HTML crudo
        if tooltip_value:
            return format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(tooltip_value), # Escapa HTML crudo
                summary
            )
        return summary
    config_notes_summary_with_html_tooltip.short_description = "Config (Tip HTML)"


    # --- Tooltips en el Formulario --- 
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # Añade tooltip HTML al texto de ayuda del campo 'name' (funciona en añadir/modificar)
        if 'name' in form.base_fields:
            name_tooltip = "Introduce el nombre <strong>único</strong> para este ítem."
            current_help = form.base_fields['name'].help_text or ''
            form.base_fields['name'].help_text = format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(name_tooltip), # Escapa HTML simple
                current_help
            )

        # Añade tooltip Markdown al widget del campo 'details'
        if 'details' in form.base_fields:
            md_content = ""
            md_attr = "data-tooltip-html" # Por defecto HTML para ayuda genérica
            if obj and hasattr(obj, 'details_tooltip_md'): # Usa contenido específico del modelo en la vista de modificar
                md_content = obj.details_tooltip_md
                md_attr = "data-tooltip-markdown"
            else: # Ayuda genérica en la vista de añadir
                md_content = 'Introduce la descripción detallada. Markdown es soportado para el tooltip en la vista de modificar.'
            form.base_fields['details'].widget.attrs.update({
                md_attr: escape(md_content)
            })

        # Añade un tooltip HTML estático al widget del campo 'config_notes' (funciona en añadir/modificar)
        if 'config_notes' in form.base_fields:
            config_tooltip = "<ul><li>Nota 1: Usa formato JSON.</li><li>Nota 2: Se requiere reinicio después del cambio.</li></ul>"
            form.base_fields['config_notes'].widget.attrs.update({
                'data-tooltip-html': escape(config_tooltip)
            })

        return form

```

### Ejemplo: Añadiendo Tooltips en Plantillas

Puedes añadir los atributos `data-` directamente a cualquier elemento HTML en tus plantillas Django (incluyendo sobrescrituras de plantillas de administración).

```html
{# En algun_template.html #}

<label for="id_my_field">Mi Campo</label>
{# Recuerda escapar el contenido si es dinámico o contiene caracteres HTML especiales #}
{% with tooltip_content="Información extra sobre <strong>Mi Campo</strong>." %}
<span data-tooltip-html="{{ tooltip_content|escape }}">?</span>
{% endwith %}
<input type="text" id="id_my_field" name="my_field">

{# Ejemplo Markdown #}
{% with md_tooltip="## Ayuda de Sección\n\nEsta sección contiene configuraciones relacionadas con X e Y." %}
<div data-tooltip-markdown="{{ md_tooltip|escape }}">
  <h2>Sección Importante</h2>
  <p>Algún contenido...</p>
</div>
{% endwith %}
```

