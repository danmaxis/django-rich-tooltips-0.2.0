# Utilisation de Base

Le plugin fonctionne en recherchant des éléments HTML avec des attributs `data-` spécifiques et en y attachant le comportement d'infobulle.

*   `data-tooltip-html="<p>Votre contenu <b>HTML</b> ici</p>"`: Utilisez ceci pour du contenu HTML brut. Le contenu sera **échappé** avant d'être placé dans l'attribut, puis décodé par le JavaScript avant le rendu.
*   `data-tooltip-markdown="# Votre Markdown\n\n*   Élément de liste"`: Utilisez ceci pour du contenu Markdown. Le contenu sera **échappé** avant d'être placé dans l'attribut, décodé par JavaScript, puis analysé par `marked.js`.

**Important :** Lorsque vous ajoutez du contenu dynamique (HTML ou Markdown) à ces attributs en Python (par exemple, dans `admin.py`), utilisez toujours `django.utils.html.escape()` sur le contenu avant de le passer à `format_html` pour la valeur de l'attribut. La partie JavaScript du plugin est conçue pour gérer ce contenu échappé.

### Exemple : Ajout d'Infobulles dans `admin.py`

Vous pouvez modifier les méthodes `list_display` ou les widgets/textes d'aide des champs de formulaire dans votre `ModelAdmin` pour inclure ces attributs. Cela fonctionne à la fois dans les vues d'ajout et de modification.

```python
# models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    config_notes = models.TextField(
        blank=True,
        help_text="Entrez les détails de configuration ici."
    )

    # Exemple : Stocker le contenu spécifique de l'infobulle dans le modèle
    details_tooltip_md = "## Champ Détails\n\nCe champ accepte du texte *multi-lignes* décrivant l'élément."
    html_tooltip_content = "<p>Ceci est du contenu <strong>HTML</strong> stocké dans le modèle.</p>"

    def get_dynamic_tooltip(self):
        return f"Infobulle dynamique basée sur le nom : {self.name}"

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

    # --- Infobulles dans l'Affichage Liste (List Display) ---

    # Exemple 1 : Infobulle depuis une méthode (texte simple)
    def name_with_dynamic_tooltip(self, obj):
        display_value = escape(obj.name)
        tooltip_value = obj.get_dynamic_tooltip() # Obtient le texte dynamique de la méthode
        if tooltip_value:
            return format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(tooltip_value), # Échappe le texte simple
                display_value
            )
        return display_value
    name_with_dynamic_tooltip.short_description = "Nom (Info Dyn)"
    name_with_dynamic_tooltip.admin_order_field = "name"

    # Exemple 2 : Infobulle Markdown depuis un champ du modèle
    def details_summary_with_markdown_tooltip(self, obj):
        summary = escape(obj.details[:50] + '...' if len(obj.details) > 50 else obj.details)
        tooltip_value = getattr(obj, 'details_tooltip_md', None) # Markdown brut
        if tooltip_value:
            return format_html(
                '<span data-tooltip-markdown="{}">{}</span>',
                escape(tooltip_value), # Échappe le Markdown brut
                summary
            )
        return summary
    details_summary_with_markdown_tooltip.short_description = "Détails (Info MD)"

    # Exemple 3 : Infobulle HTML depuis un champ du modèle
    def config_notes_summary_with_html_tooltip(self, obj):
        summary = escape(obj.config_notes[:50] + '...' if len(obj.config_notes) > 50 else obj.config_notes)
        tooltip_value = getattr(obj, 'html_tooltip_content', None) # HTML brut
        if tooltip_value:
            return format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(tooltip_value), # Échappe le HTML brut
                summary
            )
        return summary
    config_notes_summary_with_html_tooltip.short_description = "Config (Info HTML)"


    # --- Infobulles dans le Formulaire --- 
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # Ajoute une infobulle HTML au texte d'aide du champ 'name' (fonctionne en ajout/modification)
        if 'name' in form.base_fields:
            name_tooltip = "Entrez le nom <strong>unique</strong> pour cet élément."
            current_help = form.base_fields['name'].help_text or ''
            form.base_fields['name'].help_text = format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(name_tooltip), # Échappe le HTML simple
                current_help
            )

        # Ajoute une infobulle Markdown au widget du champ 'details'
        if 'details' in form.base_fields:
            md_content = ""
            md_attr = "data-tooltip-html" # Par défaut HTML pour l'aide générique
            if obj and hasattr(obj, 'details_tooltip_md'): # Utilise le contenu spécifique du modèle dans la vue de modification
                md_content = obj.details_tooltip_md
                md_attr = "data-tooltip-markdown"
            else: # Aide générique dans la vue d'ajout
                md_content = 'Entrez la description détaillée. Markdown est supporté pour l'infobulle dans la vue de modification.'
            form.base_fields['details'].widget.attrs.update({
                md_attr: escape(md_content)
            })

        # Ajoute une infobulle HTML statique au widget du champ 'config_notes' (fonctionne en ajout/modification)
        if 'config_notes' in form.base_fields:
            config_tooltip = "<ul><li>Note 1 : Utilisez le format JSON.</li><li>Note 2 : Redémarrage requis après modification.</li></ul>"
            form.base_fields['config_notes'].widget.attrs.update({
                'data-tooltip-html': escape(config_tooltip)
            })

        return form

```

### Exemple : Ajout d'Infobulles dans les Templates

Vous pouvez ajouter les attributs `data-` directement à n'importe quel élément HTML dans vos templates Django (y compris les surcharges de templates d'administration).

```html
{# Dans un_template.html #}

<label for="id_my_field">Mon Champ</label>
{# N'oubliez pas d'échapper le contenu s'il est dynamique ou contient des caractères HTML spéciaux #}
{% with tooltip_content="Information supplémentaire sur <strong>Mon Champ</strong>." %}
<span data-tooltip-html="{{ tooltip_content|escape }}">?</span>
{% endwith %}
<input type="text" id="id_my_field" name="my_field">

{# Exemple Markdown #}
{% with md_tooltip="## Aide de Section\n\nCette section contient des paramètres liés à X et Y." %}
<div data-tooltip-markdown="{{ md_tooltip|escape }}">
  <h2>Section Importante</h2>
  <p>Du contenu...</p>
</div>
{% endwith %}
```

