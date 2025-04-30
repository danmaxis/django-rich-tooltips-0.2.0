# Installation

**Note:** This package is not yet available on PyPI.

1.  **Install the package:**
    ```bash
    # Once available on PyPI:
    # pip install django-rich-tooltips

    # For now, install it directly from the source/repository:
    pip install -e .
    # Or from a git repository:
    # pip install git+https://github.com/yourusername/django-rich-tooltips.git
    ```

2.  **Add `rich_tooltips` to your `INSTALLED_APPS` in `settings.py`:**

    Make sure it comes *before* `django.contrib.admin` if you intend to override admin templates (like `base_site.html`).

    ```python
    # settings.py
    INSTALLED_APPS = [
        # ... other apps
        'rich_tooltips', # Add the plugin app
        'django.contrib.admin',
        # ... other apps
    ]
    ```

3.  **Template Setup:**
    The plugin relies on JavaScript and CSS files being included in your admin pages. It provides a `templates/admin/base_site.html` that extends the default one and includes the necessary files via CDN (for `marked.js`) and static files (for the plugin's JS/CSS).

    *   **If you DO NOT override `admin/base_site.html`:** You should be all set, as Django will automatically pick up the plugin's template due to the order in `INSTALLED_APPS`.
    *   **If you DO override `admin/base_site.html`:** You need to manually include the necessary static files in your custom `base_site.html` or ensure your template extends `rich_tooltips/templates/admin/base_site.html`.

        Add the following within your `<head>` or appropriate blocks:

        ```html
        {% extends "admin/base_site.html" %} {# Or your own base #}
        {% load static %}

        {% block extrastyle %}
          {{ block.super }}
          <link rel="stylesheet" type="text/css" href="{% static 'rich_tooltips/css/rich_tooltips.css' %}">
        {% endblock %}

        {% block extrahead %}
          {{ block.super }}
          {# Load marked.js library from CDN #}
          <script src="https://cdn.jsdelivr.net/npm/marked@15.0.11/lib/marked.umd.min.js"></script>
          {# Load plugin JS deferred #}
          <script src="{% static 'rich_tooltips/js/rich_tooltips.js' %}" defer></script>
        {% endblock %}
        ```

4.  **Collect Static Files:**
    Run `python manage.py collectstatic` to ensure the plugin's static files (`rich_tooltips.js`, `rich_tooltips.css`) are collected into your `STATIC_ROOT`.

