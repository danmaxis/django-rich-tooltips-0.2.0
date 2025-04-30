# 安装

**注意：** 此软件包尚未在 PyPI 上提供。

1.  **安装软件包：**
    ```bash
    # 在 PyPI 上可用后：
    # pip install django-rich-tooltips

    # 目前，请直接从源代码/存储库安装：
    pip install -e .
    # 或从 git 存储库安装：
    # pip install git+https://github.com/yourusername/django-rich-tooltips.git
    ```

2.  **在 `settings.py` 中将 `rich_tooltips` 添加到您的 `INSTALLED_APPS`：**

    如果您打算覆盖管理模板（如 `base_site.html`），请确保它位于 `django.contrib.admin` *之前*。

    ```python
    # settings.py
    INSTALLED_APPS = [
        # ... 其他应用程序
        'rich_tooltips', # 添加插件应用程序
        'django.contrib.admin',
        # ... 其他应用程序
    ]
    ```

3.  **模板设置：**
    该插件依赖于包含在您的管理页面中的 JavaScript 和 CSS 文件。它提供了一个 `templates/admin/base_site.html`，该模板扩展了默认模板，并通过 CDN（用于 `marked.js`）和静态文件（用于插件的 JS/CSS）包含了必要的文件。

    *   **如果您不覆盖 `admin/base_site.html`：** 您应该已经准备就绪，因为 Django 会根据 `INSTALLED_APPS` 中的顺序自动选取插件的模板。
    *   **如果您覆盖 `admin/base_site.html`：** 您需要手动将必要的静态文件包含在您的自定义 `base_site.html` 中，或确保您的模板扩展了 `rich_tooltips/templates/admin/base_site.html`。

        在您的 `<head>` 或适当的块中添加以下内容：

        ```html
        {% extends "admin/base_site.html" %} {# 或您自己的基础模板 #}
        {% load static %}

        {% block extrastyle %}
          {{ block.super }}
          <link rel="stylesheet" type="text/css" href="{% static 'rich_tooltips/css/rich_tooltips.css' %}">
        {% endblock %}

        {% block extrahead %}
          {{ block.super }}
          {# 从 CDN 加载 marked.js 库 #}
          <script src="https://cdn.jsdelivr.net/npm/marked@15.0.11/lib/marked.umd.min.js"></script>
          {# 延迟加载插件 JS #}
          <script src="{% static 'rich_tooltips/js/rich_tooltips.js' %}" defer></script>
        {% endblock %}
        ```

4.  **收集静态文件：**
    运行 `python manage.py collectstatic` 以确保插件的静态文件（`rich_tooltips.js`、`rich_tooltips.css`）被收集到您的 `STATIC_ROOT` 中。

