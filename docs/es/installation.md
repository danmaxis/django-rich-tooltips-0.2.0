# Instalación

**Nota:** Este paquete aún no está disponible en PyPI.

1.  **Instala el paquete:**
    ```bash
    # Una vez disponible en PyPI:
    # pip install django-rich-tooltips

    # Por ahora, instálalo directamente desde la fuente/repositorio:
    pip install -e .
    # O desde un repositorio git:
    # pip install git+https://github.com/yourusername/django-rich-tooltips.git
    ```

2.  **Añade `rich_tooltips` a tus `INSTALLED_APPS` en `settings.py`:**

    Asegúrate de que venga *antes* de `django.contrib.admin` si tienes la intención de sobrescribir plantillas de administración (como `base_site.html`).

    ```python
    # settings.py
    INSTALLED_APPS = [
        # ... otras apps
        'rich_tooltips', # Añade la app del plugin
        'django.contrib.admin',
        # ... otras apps
    ]
    ```

3.  **Configuración de Plantilla:**
    El plugin depende de que los archivos JavaScript y CSS se incluyan en tus páginas de administración. Proporciona un `templates/admin/base_site.html` que extiende el predeterminado e incluye los archivos necesarios a través de CDN (para `marked.js`) y archivos estáticos (para el JS/CSS del plugin).

    *   **Si NO sobrescribes `admin/base_site.html`:** Deberías estar listo, ya que Django recogerá automáticamente la plantilla del plugin debido al orden en `INSTALLED_APPS`.
    *   **Si SÍ sobrescribes `admin/base_site.html`:** Necesitas incluir manualmente los archivos estáticos necesarios en tu `base_site.html` personalizado o asegurarte de que tu plantilla extienda `rich_tooltips/templates/admin/base_site.html`.

        Añade lo siguiente dentro de tu `<head>` o bloques apropiados:

        ```html
        {% extends "admin/base_site.html" %} {# O tu propia base #}
        {% load static %}

        {% block extrastyle %}
          {{ block.super }}
          <link rel="stylesheet" type="text/css" href="{% static 'rich_tooltips/css/rich_tooltips.css' %}">
        {% endblock %}

        {% block extrahead %}
          {{ block.super }}
          {# Carga la biblioteca marked.js desde CDN #}
          <script src="https://cdn.jsdelivr.net/npm/marked@15.0.11/lib/marked.umd.min.js"></script>
          {# Carga el JS del plugin diferido #}
          <script src="{% static 'rich_tooltips/js/rich_tooltips.js' %}" defer></script>
        {% endblock %}
        ```

4.  **Recolectar Archivos Estáticos:**
    Ejecuta `python manage.py collectstatic` para asegurar que los archivos estáticos del plugin (`rich_tooltips.js`, `rich_tooltips.css`) se recolecten en tu `STATIC_ROOT`.

