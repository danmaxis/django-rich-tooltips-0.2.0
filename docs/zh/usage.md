# 基本用法

该插件通过查找具有特定 `data-` 属性的 HTML 元素并为其附加工具提示行为来工作。

*   `data-tooltip-html="<p>您的 <b>HTML</b> 内容在此</p>"`: 用于原始 HTML 内容。内容在放入属性之前将被 **转义**，然后在渲染之前由 JavaScript 解码。
*   `data-tooltip-markdown="# 您的 Markdown\n\n*   列表项"`: 用于 Markdown 内容。内容在放入属性之前将被 **转义**，由 JavaScript 解码，然后由 `marked.js` 解析。

**重要提示：** 在 Python 中（例如，在 `admin.py` 中）向这些属性添加动态内容（HTML 或 Markdown）时，请始终在将内容传递给 `format_html` 以获取属性值之前，对内容使用 `django.utils.html.escape()`。插件的 JavaScript 部分旨在处理此转义内容。

### 示例：在 `admin.py` 中添加工具提示

您可以在 `ModelAdmin` 中修改 `list_display` 方法或表单字段的 widgets/help text 以包含这些属性。这在添加和更改视图中都有效。

```python
# models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    config_notes = models.TextField(
        blank=True,
        help_text="在此输入配置详细信息。"
    )

    # 示例：在模型中存储特定的工具提示内容
    details_tooltip_md = "## 详细信息字段\n\n此字段接受描述项目的*多行*文本。"
    html_tooltip_content = "<p>这是存储在模型中的 <strong>HTML</strong> 内容。</p>"

    def get_dynamic_tooltip(self):
        return f"基于名称的动态工具提示：{self.name}"

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

    # --- 列表显示工具提示 ---

    # 示例 1：来自方法的工具提示（纯文本）
    def name_with_dynamic_tooltip(self, obj):
        display_value = escape(obj.name)
        tooltip_value = obj.get_dynamic_tooltip() # 从方法获取动态文本
        if tooltip_value:
            return format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(tooltip_value), # 转义纯文本
                display_value
            )
        return display_value
    name_with_dynamic_tooltip.short_description = "名称（动态提示）"
    name_with_dynamic_tooltip.admin_order_field = "name"

    # 示例 2：来自模型字段的 Markdown 工具提示
    def details_summary_with_markdown_tooltip(self, obj):
        summary = escape(obj.details[:50] + '...' if len(obj.details) > 50 else obj.details)
        tooltip_value = getattr(obj, 'details_tooltip_md', None) # 原始 Markdown
        if tooltip_value:
            return format_html(
                '<span data-tooltip-markdown="{}">{}</span>',
                escape(tooltip_value), # 转义原始 Markdown
                summary
            )
        return summary
    details_summary_with_markdown_tooltip.short_description = "详细信息（MD 提示）"

    # 示例 3：来自模型字段的 HTML 工具提示
    def config_notes_summary_with_html_tooltip(self, obj):
        summary = escape(obj.config_notes[:50] + '...' if len(obj.config_notes) > 50 else obj.config_notes)
        tooltip_value = getattr(obj, 'html_tooltip_content', None) # 原始 HTML
        if tooltip_value:
            return format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(tooltip_value), # 转义原始 HTML
                summary
            )
        return summary
    config_notes_summary_with_html_tooltip.short_description = "配置（HTML 提示）"


    # --- 表单工具提示 --- 
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # 将 HTML 工具提示添加到 'name' 字段的帮助文本中（在添加/更改时有效）
        if 'name' in form.base_fields:
            name_tooltip = "输入此项目的<strong>唯一名称</strong>。"
            current_help = form.base_fields['name'].help_text or ''
            form.base_fields['name'].help_text = format_html(
                '<span data-tooltip-html="{}">{}</span>',
                escape(name_tooltip), # 转义简单 HTML
                current_help
            )

        # 将 Markdown 工具提示添加到 'details' 字段的 widget 中
        if 'details' in form.base_fields:
            md_content = ""
            md_attr = "data-tooltip-html" # 默认为 HTML 以提供通用帮助
            if obj and hasattr(obj, 'details_tooltip_md'): # 在更改视图中使用模型中的特定内容
                md_content = obj.details_tooltip_md
                md_attr = "data-tooltip-markdown"
            else: # 在添加视图中提供通用帮助
                md_content = '输入详细描述。更改视图中的工具提示支持 Markdown。'
            form.base_fields['details'].widget.attrs.update({
                md_attr: escape(md_content)
            })

        # 将静态 HTML 工具提示添加到 'config_notes' 字段的 widget 中（在添加/更改时有效）
        if 'config_notes' in form.base_fields:
            config_tooltip = "<ul><li>注意 1：使用 JSON 格式。</li><li>注意 2：更改后需要重新启动。</li></ul>"
            form.base_fields['config_notes'].widget.attrs.update({
                'data-tooltip-html': escape(config_tooltip)
            })

        return form

```

### 示例：在模板中添加工具提示

您可以将 `data-` 属性直接添加到 Django 模板中的任何 HTML 元素（包括管理模板覆盖）。

```html
{# 在某个 template.html 中 #}

<label for="id_my_field">我的字段</label>
{# 如果内容是动态的或包含特殊 HTML 字符，请记住转义内容 #}
{% with tooltip_content="关于<strong>我的字段</strong>的额外信息。" %}
<span data-tooltip-html="{{ tooltip_content|escape }}">?</span>
{% endwith %}
<input type="text" id="id_my_field" name="my_field">

{# Markdown 示例 #}
{% with md_tooltip="## 区域帮助\n\n此区域包含与 X 和 Y 相关的设置。" %}
<div data-tooltip-markdown="{{ md_tooltip|escape }}">
  <h2>重要区域</h2>
  <p>一些内容...</p>
</div>
{% endwith %}
```

