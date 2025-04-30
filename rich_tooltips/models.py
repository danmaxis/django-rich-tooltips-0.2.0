# -*- coding: utf-8 -*-
from django.db import models

class TooltipTestModel(models.Model):
    """A simple model for testing tooltips in the admin."""
    name = models.CharField(max_length=100)
    description = models.TextField(
        help_text="This field will have a basic HTML tooltip."
    )
    markdown_field = models.TextField(
        help_text="This field will have a Markdown tooltip (requires JS library).",
        blank=True
    )

    # Example tooltip content stored directly in the model (can be dynamic)
    tooltip_content_html = "<p>This is an <strong>HTML</strong> tooltip defined in the model!</p><ul><li>Item 1</li><li>Item 2</li></ul>"
    tooltip_content_markdown = "## Markdown Tooltip\n\nThis content is written in *Markdown* and should be rendered by the JS library.\n\n- Point A\n- Point B"

    def __str__(self):
        return self.name

