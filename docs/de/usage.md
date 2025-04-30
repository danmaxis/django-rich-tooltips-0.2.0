# Grundlegende Verwendung

Das Plugin funktioniert, indem es nach HTML-Elementen mit spezifischen `data-`-Attributen sucht und ihnen das Tooltip-Verhalten hinzufügt.

*   `data-tooltip-html="<p>Ihr <b>HTML</b>-Inhalt hier</p>"`: Verwenden Sie dies für reinen HTML-Inhalt. Der Inhalt wird **escaped**, bevor er in das Attribut eingefügt wird, und dann vom JavaScript dekodiert, bevor er gerendert wird.
*   `data-tooltip-markdown="# Ihr Markdown\n\n*   Listenelement"`: Verwenden Sie dies für Markdown-Inhalt. Der Inhalt wird **escaped**, bevor er in das Attribut eingefügt wird, vom JavaScript dekodiert und dann von `marked.js` geparst.

**Wichtig:** Wenn Sie dynamischen Inhalt (HTML oder Markdown) zu diesen Attributen in Python hinzufügen (z. B. in `admin.py`), verwenden Sie immer `django.utils.html.escape()` für den Inhalt, bevor Sie ihn an `format_html` für den Attributwert übergeben. Der JavaScript-Teil des Plugins ist darauf ausgelegt, diesen escaped Inhalt zu verarbeiten.

### Beispiel: Hinzufügen von Tooltips in `admin.py`

Sie können die `list_display`-Methoden oder die Widgets/Hilfetexte der Formularfelder in Ihrem `ModelAdmin` ändern, um diese Attribute einzuschließen. Dies funktioniert sowohl in den Ansichten zum Hinzufügen als auch zum Ändern.

```python
# models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    config_notes = models.TextField(
        blank=True,
        help_text="Geben Sie hier Konfigurationsdetails ein."
    )

    # Beispiel: Spezifischen Tooltip-Inhalt im Modell speichern
    details_tooltip_md = "## Feld Details\n\nDieses Feld akzeptiert *mehrzeiligen* Text zur Beschreibung des Elements."
    html_tooltip_content = "<p>Dies ist im Modell gespeicherter <strong>HTML</strong>-Inhalt.</p>"

    def get_dynamic_tooltip(self):
        return f"Dynamischer Tooltip basierend auf dem Namen: {self.name}"

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

    # --- Tooltips in der Listenanzeige (List Display) ---

    # Beispiel 1: Tooltip aus einer Methode (einfacher Text)
    def name_with_dynamic_tooltip(self, obj):
        display_value = escape(obj.name)
        tooltip_value = obj.get_dynamic_tooltip() # Dynamischen Text aus Methode holen
        if tooltip_value:
            return format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(tooltip_value), # Einfachen Text escapen
                display_value
            )
        return display_value
    name_with_dynamic_tooltip.short_description = "Name (Dyn. Tipp)"
    name_with_dynamic_tooltip.admin_order_field = "name"

    # Beispiel 2: Markdown-Tooltip aus einem Modellfeld
    def details_summary_with_markdown_tooltip(self, obj):
        summary = escape(obj.details[:50] + '...' if len(obj.details) > 50 else obj.details)
        tooltip_value = getattr(obj, 'details_tooltip_md', None) # Rohes Markdown
        if tooltip_value:
            return format_html(
                '<span data-tooltip-markdown="{}">{}</span>',
                escape(tooltip_value), # Rohes Markdown escapen
                summary
            )
        return summary
    details_summary_with_markdown_tooltip.short_description = "Details (MD Tipp)"

    # Beispiel 3: HTML-Tooltip aus einem Modellfeld
    def config_notes_summary_with_html_tooltip(self, obj):
        summary = escape(obj.config_notes[:50] + '...' if len(obj.config_notes) > 50 else obj.config_notes)
        tooltip_value = getattr(obj, 'html_tooltip_content', None) # Rohes HTML
        if tooltip_value:
            return format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(tooltip_value), # Rohes HTML escapen
                summary
            )
        return summary
    config_notes_summary_with_html_tooltip.short_description = "Konfig (HTML Tipp)"


    # --- Formular-Tooltips --- 
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # HTML-Tooltip zum Hilfetext des Feldes 'name' hinzufügen (funktioniert bei Hinzufügen/Ändern)
        if 'name' in form.base_fields:
            name_tooltip = "Geben Sie den <strong>eindeutigen Namen</strong> für dieses Element ein."
            current_help = form.base_fields['name'].help_text or ''
            form.base_fields['name'].help_text = format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(name_tooltip), # Einfaches HTML escapen
                current_help
            )

        # Markdown-Tooltip zum Widget des Feldes 'details' hinzufügen
        if 'details' in form.base_fields:
            md_content = ""
            md_attr = "data-tooltip-html" # Standardmäßig HTML für allgemeine Hilfe
            if obj and hasattr(obj, 'details_tooltip_md'): # Spezifischen Inhalt aus Modell in Änderungsansicht verwenden
                md_content = obj.details_tooltip_md
                md_attr = "data-tooltip-markdown"
            else: # Allgemeine Hilfe in Hinzufügeansicht
                md_content = 'Geben Sie eine detaillierte Beschreibung ein. Markdown wird für den Tooltip in der Änderungsansicht unterstützt.'
            form.base_fields['details'].widget.attrs.update({
                md_attr: escape(md_content)
            })

        # Statischen HTML-Tooltip zum Widget des Feldes 'config_notes' hinzufügen (funktioniert bei Hinzufügen/Ändern)
        if 'config_notes' in form.base_fields:
            config_tooltip = "<ul><li>Hinweis 1: Verwenden Sie das JSON-Format.</li><li>Hinweis 2: Neustart nach Änderung erforderlich.</li></ul>"
            form.base_fields['config_notes'].widget.attrs.update({
                'data-tooltip-html': escape(config_tooltip)
            })

        return form

```

### Beispiel: Hinzufügen von Tooltips in Templates

Sie können die `data-`-Attribute direkt zu jedem HTML-Element in Ihren Django-Templates hinzufügen (einschließlich Überschreibungen von Admin-Templates).

```html
{# In irgendeiner_template.html #}

<label for="id_my_field">Mein Feld</label>
{# Denken Sie daran, den Inhalt zu escapen, wenn er dynamisch ist oder spezielle HTML-Zeichen enthält #}
{% with tooltip_content="Zusätzliche Informationen über <strong>Mein Feld</strong>." %}
<span data-tooltip-html="{{ tooltip_content|escape }}">?</span>
{% endwith %}
<input type="text" id="id_my_field" name="my_field">

{# Markdown-Beispiel #}
{% with md_tooltip="## Abschnittshilfe\n\nDieser Abschnitt enthält Einstellungen zu X und Y." %}
<div data-tooltip-markdown="{{ md_tooltip|escape }}">
  <h2>Wichtiger Abschnitt</h2>
  <p>Etwas Inhalt...</p>
</div>
{% endwith %}
```

