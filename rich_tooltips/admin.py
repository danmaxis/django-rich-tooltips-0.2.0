# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import format_html, escape
from .models import TooltipTestModel

@admin.register(TooltipTestModel)
class TooltipTestModelAdmin(admin.ModelAdmin):
    list_display = ("name_with_tooltip", "description_with_tooltip", "markdown_field_placeholder")

    # --- Tooltip for 'name' field (dynamic text from method) ---
    def name_with_tooltip(self, obj):
        display_value = escape(obj.name) # Escape display value for safety
        tooltip_value = self.get_name_tooltip_content(obj) # Get dynamic text
        tooltip_attr = "data-tooltip-html"
        if tooltip_value:
            # Escape the dynamic text before putting it in the HTML attribute
            return format_html(
                '<span {}="{}">{}</span>',
                tooltip_attr,
                escape(tooltip_value),
                display_value
            )
        return display_value
    name_with_tooltip.short_description = "Name (Hover Me)"
    name_with_tooltip.admin_order_field = "name" # Allow sorting

    def get_name_tooltip_content(self, obj):
        # Example method providing dynamic tooltip content (simple text)
        return f"Tooltip for item: {obj.name}. Description length: {len(obj.description)}"

    # --- Tooltip for 'description' field (HTML from model field) ---
    def description_with_tooltip(self, obj):
        display_value = escape(obj.description[:50] + "..." if len(obj.description) > 50 else obj.description) # Escape display value
        # Get tooltip content from a field on the model (assumed to be safe HTML)
        tooltip_value = getattr(obj, 'tooltip_content_html', None)
        tooltip_attr = "data-tooltip-html"
        if tooltip_value:
            # Escape the raw HTML before putting it in the HTML attribute
            # The JS will decode this when setting innerHTML
            return format_html(
                '<span {}="{}">{}</span>',
                tooltip_attr,
                escape(tooltip_value),
                display_value
            )
        return display_value
    description_with_tooltip.short_description = "Description (Hover Me)"

    # --- Tooltip for 'markdown_field' (Markdown from model field) ---
    def markdown_field_placeholder(self, obj):
        display_value = "(MD)" # Shorter placeholder
        # Get tooltip content from a field on the model
        tooltip_value = getattr(obj, 'tooltip_content_markdown', None) # Raw Markdown
        tooltip_attr = "data-tooltip-markdown"
        if tooltip_value:
            # Escape the raw Markdown before putting it in the HTML attribute
            # JS will need to decode this before passing to marked.parse()
            return format_html(
                '<span {}="{}">{}</span>',
                tooltip_attr,
                escape(tooltip_value),
                display_value
            )
        return display_value
    markdown_field_placeholder.short_description = "Markdown Field (Hover Me)"


    # --- Form customization (remains the same, escaping already applied) ---
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # Help text tooltip (simple text)
        if "name" in form.base_fields:
            name_tooltip = "Enter the primary name for this item. This is a required field."
            current_help_text = form.base_fields["name"].help_text or ""
            form.base_fields["name"].help_text = format_html(
                "<span data-tooltip-html=\"{}\">{}</span>",
                escape(name_tooltip), # Escape simple text
                current_help_text
            )

        # Widget tooltips
        if "description" in form.base_fields:
            desc_tooltip_content = ""
            if obj and obj.tooltip_content_html:
                desc_tooltip_content = obj.tooltip_content_html # Assumed safe HTML
            else:
                desc_tooltip_content = "Provide a detailed description. Supports basic HTML formatting in the tooltip on the change view." # Simple text/HTML
            form.base_fields["description"].widget.attrs.update({
                "data-tooltip-html": escape(desc_tooltip_content) # Escape for attribute
            })

        if "markdown_field" in form.base_fields:
            md_tooltip_content = ""
            md_attr = "data-tooltip-html"
            if obj and obj.tooltip_content_markdown:
                md_tooltip_content = obj.tooltip_content_markdown # Raw Markdown
                md_attr = "data-tooltip-markdown"
            else:
                md_tooltip_content = "Enter content using Markdown syntax. It will be rendered as HTML in the tooltip on the change view." # Simple text/HTML
            form.base_fields["markdown_field"].widget.attrs.update({
                md_attr: escape(md_tooltip_content) # Escape for attribute
            })

        return form

