# Installation

**Hinweis:** Dieses Paket ist noch nicht auf PyPI verfügbar.

1.  **Installieren Sie das Paket:**
    ```bash
    # Sobald auf PyPI verfügbar:
    # pip install django-rich-tooltips

    # Installieren Sie es vorerst direkt aus der Quelle/dem Repository:
    pip install -e .
    # Oder aus einem Git-Repository:
    # pip install git+https://github.com/yourusername/django-rich-tooltips.git
    ```

2.  **Fügen Sie `rich_tooltips` zu Ihren `INSTALLED_APPS` in `settings.py` hinzu:**

    Stellen Sie sicher, dass es *vor* `django.contrib.admin` steht, wenn Sie Admin-Templates (wie `base_site.html`) überschreiben möchten.

    ```python
    # settings.py
    INSTALLED_APPS = [
        # ... andere Apps
        'rich_tooltips', # Fügen Sie die Plugin-App hinzu
        'django.contrib.admin',
        # ... andere Apps
    ]
    ```

3.  **Template-Setup:**
    Das Plugin benötigt JavaScript- und CSS-Dateien, die in Ihre Admin-Seiten eingebunden werden. Es stellt ein `templates/admin/base_site.html` bereit, das das Standard-Template erweitert und die notwendigen Dateien über CDN (für `marked.js`) und statische Dateien (für das JS/CSS des Plugins) einbindet.

    *   **Wenn Sie `admin/base_site.html` NICHT überschreiben:** Sie sollten bereit sein, da Django das Template des Plugins aufgrund der Reihenfolge in `INSTALLED_APPS` automatisch aufnimmt.
    *   **Wenn Sie `admin/base_site.html` ÜBERSCHREIBEN:** Sie müssen die notwendigen statischen Dateien manuell in Ihr benutzerdefiniertes `base_site.html` einbinden oder sicherstellen, dass Ihr Template `rich_tooltips/templates/admin/base_site.html` erweitert.

        Fügen Sie Folgendes in Ihren `<head>` oder entsprechende Blöcke ein:

        ```html
        {% extends "admin/base_site.html" %} {# Oder Ihre eigene Basis #}
        {% load static %}

        {% block extrastyle %}
          {{ block.super }}
          <link rel="stylesheet" type="text/css" href="{% static 'rich_tooltips/css/rich_tooltips.css' %}">
        {% endblock %}

        {% block extrahead %}
          {{ block.super }}
          {# Laden Sie die marked.js-Bibliothek vom CDN #}
          <script src="https://cdn.jsdelivr.net/npm/marked@15.0.11/lib/marked.umd.min.js"></script>
          {# Laden Sie das Plugin-JS verzögert #}
          <script src="{% static 'rich_tooltips/js/rich_tooltips.js' %}" defer></script>
        {% endblock %}
        ```

4.  **Statische Dateien sammeln:**
    Führen Sie `python manage.py collectstatic` aus, um sicherzustellen, dass die statischen Dateien des Plugins (`rich_tooltips.js`, `rich_tooltips.css`) in Ihrem `STATIC_ROOT` gesammelt werden.

