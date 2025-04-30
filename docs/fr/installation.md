# Installation

**Note :** Ce paquet n'est pas encore disponible sur PyPI.

1.  **Installez le paquet :**
    ```bash
    # Une fois disponible sur PyPI :
    # pip install django-rich-tooltips

    # Pour l'instant, installez-le directement depuis la source/le dépôt :
    pip install -e .
    # Ou depuis un dépôt git :
    # pip install git+https://github.com/yourusername/django-rich-tooltips.git
    ```

2.  **Ajoutez `rich_tooltips` à vos `INSTALLED_APPS` dans `settings.py` :**

    Assurez-vous qu'il vienne *avant* `django.contrib.admin` si vous avez l'intention de surcharger les templates d'administration (comme `base_site.html`).

    ```python
    # settings.py
    INSTALLED_APPS = [
        # ... autres applications
        'rich_tooltips', # Ajoutez l'application du plugin
        'django.contrib.admin',
        # ... autres applications
    ]
    ```

3.  **Configuration du Template :**
    Le plugin dépend de l'inclusion de fichiers JavaScript et CSS dans vos pages d'administration. Il fournit un `templates/admin/base_site.html` qui étend celui par défaut et inclut les fichiers nécessaires via CDN (pour `marked.js`) et fichiers statiques (pour le JS/CSS du plugin).

    *   **Si vous NE surchargez PAS `admin/base_site.html` :** Vous devriez être prêt, car Django récupérera automatiquement le template du plugin grâce à l'ordre dans `INSTALLED_APPS`.
    *   **Si vous SURCHARGEZ `admin/base_site.html` :** Vous devez inclure manuellement les fichiers statiques nécessaires dans votre `base_site.html` personnalisé ou vous assurer que votre template étend `rich_tooltips/templates/admin/base_site.html`.

        Ajoutez ce qui suit dans votre `<head>` ou les blocs appropriés :

        ```html
        {% extends "admin/base_site.html" %} {# Ou votre propre base #}
        {% load static %}

        {% block extrastyle %}
          {{ block.super }}
          <link rel="stylesheet" type="text/css" href="{% static 'rich_tooltips/css/rich_tooltips.css' %}">
        {% endblock %}

        {% block extrahead %}
          {{ block.super }}
          {# Charge la bibliothèque marked.js depuis le CDN #}
          <script src="https://cdn.jsdelivr.net/npm/marked@15.0.11/lib/marked.umd.min.js"></script>
          {# Charge le JS du plugin en différé #}
          <script src="{% static 'rich_tooltips/js/rich_tooltips.js' %}" defer></script>
        {% endblock %}
        ```

4.  **Collecter les Fichiers Statiques :**
    Exécutez `python manage.py collectstatic` pour vous assurer que les fichiers statiques du plugin (`rich_tooltips.js`, `rich_tooltips.css`) sont collectés dans votre `STATIC_ROOT`.

