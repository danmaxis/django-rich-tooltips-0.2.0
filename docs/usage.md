# Basic Usage

The plugin works by looking for HTML elements with specific `data-` attributes and attaching tooltip behavior to them.

*   `data-tooltip-html="<p>Your <b>HTML</b> content here</p>"`: Use this for raw HTML content. The content will be **escaped** before being placed in the attribute, and then decoded by the JavaScript before rendering.
*   `data-tooltip-markdown="# Your Markdown\n\n*   List item"`: Use this for Markdown content. The content will be **escaped** before being placed in the attribute, decoded by JavaScript, and then parsed by `marked.js`.

**Important:** When adding dynamic content (HTML or Markdown) to these attributes in Python (e.g., in `admin.py`), always use `django.utils.html.escape()` on the content before passing it to `format_html` for the attribute value. The JavaScript part of the plugin is designed to handle this escaped content.

### Example: Adding Tooltips in `admin.py`

You can modify the `list_display` methods or the form field widgets/help text within your `ModelAdmin` to include these attributes. This works on both the add and change views.

```python
# models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    config_notes = models.TextField(
        blank=True,
        help_text="Enter configuration details here."
    )

    # Example: Store specific tooltip content in the model
    details_tooltip_md = "## Details Field\n\nThis field accepts *multi-line* text describing the item."
    html_tooltip_content = "<p>This is <strong>HTML</strong> content stored in the model.</p>"

    def get_dynamic_tooltip(self):
        return f"Dynamic tooltip based on name: {self.name}"

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

    # --- List Display Tooltips ---

    # Example 1: Tooltip from a method (simple text)
    def name_with_dynamic_tooltip(self, obj):
        display_value = escape(obj.name)
        tooltip_value = obj.get_dynamic_tooltip() # Get dynamic text from method
        if tooltip_value:
            return format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(tooltip_value), # Escape simple text
                display_value
            )
        return display_value
    name_with_dynamic_tooltip.short_description = "Name (Dynamic Tip)"
    name_with_dynamic_tooltip.admin_order_field = "name"

    # Example 2: Markdown Tooltip from a model field
    def details_summary_with_markdown_tooltip(self, obj):
        summary = escape(obj.details[:50] + '...' if len(obj.details) > 50 else obj.details)
        tooltip_value = getattr(obj, 'details_tooltip_md', None) # Raw Markdown
        if tooltip_value:
            return format_html(
                '<span data-tooltip-markdown="{}">{}</span>',
                escape(tooltip_value), # Escape raw Markdown
                summary
            )
        return summary
    details_summary_with_markdown_tooltip.short_description = "Details (MD Tip)"

    # Example 3: HTML Tooltip from a model field
    def config_notes_summary_with_html_tooltip(self, obj):
        summary = escape(obj.config_notes[:50] + '...' if len(obj.config_notes) > 50 else obj.config_notes)
        tooltip_value = getattr(obj, 'html_tooltip_content', None) # Raw HTML
        if tooltip_value:
            return format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(tooltip_value), # Escape raw HTML
                summary
            )
        return summary
    config_notes_summary_with_html_tooltip.short_description = "Config (HTML Tip)"


    # --- Form Tooltips --- 
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # Add HTML tooltip to the 'name' field's help text (works on add/change)
        if 'name' in form.base_fields:
            name_tooltip = "Enter the <strong>unique name</strong> for this item."
            current_help = form.base_fields['name'].help_text or ''
            form.base_fields['name'].help_text = format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(name_tooltip), # Escape simple HTML
                current_help
            )

        # Add Markdown tooltip to the 'details' field widget
        if 'details' in form.base_fields:
            md_content = ""
            md_attr = "data-tooltip-html" # Default to HTML for generic help
            if obj and hasattr(obj, 'details_tooltip_md'): # Use specific content from model on change view
                md_content = obj.details_tooltip_md
                md_attr = "data-tooltip-markdown"
            else: # Generic help on add view
                md_content = 'Enter detailed description. Markdown is supported for the tooltip on the change view.'
            form.base_fields['details'].widget.attrs.update({
                md_attr: escape(md_content)
            })

        # Add a static HTML tooltip to the 'config_notes' field widget (works on add/change)
        if 'config_notes' in form.base_fields:
            config_tooltip = "<ul><li>Note 1: Use JSON format.</li><li>Note 2: Restart required after change.</li></ul>"
            form.base_fields['config_notes'].widget.attrs.update({
                'data-tooltip-html': escape(config_tooltip)
            })

        return form

```

### Example: Adding Tooltips in Templates

You can add the `data-` attributes directly to any HTML element in your Django templates (including admin template overrides).

```html
{# In some_template.html #}

<label for="id_my_field">My Field</label>
{# Remember to escape the content if it's dynamic or contains special HTML chars #}
{% with tooltip_content="Extra information about <strong>My Field</strong>." %}
<span data-tooltip-html="{{ tooltip_content|escape }}">?</span>
{% endwith %}
<input type="text" id="id_my_field" name="my_field">

{# Markdown example #}
{% with md_tooltip="## Section Help\n\nThis section contains settings related to X and Y." %}
<div data-tooltip-markdown="{{ md_tooltip|escape }}">
  <h2>Important Section</h2>
  <p>Some content...</p>
</div>
{% endwith %}
```

