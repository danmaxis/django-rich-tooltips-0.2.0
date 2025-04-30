# Instalação

**Observação:** Este pacote ainda não está disponível no PyPI.

1.  **Instale o pacote:**
    ```bash
    # Quando estiver disponível no PyPI:
    # pip install django-rich-tooltips

    # Por enquanto, instale diretamente do código-fonte/repositório:
    pip install -e .
    # Ou de um repositório git:
    # pip install git+https://github.com/yourusername/django-rich-tooltips.git
    ```

2.  **Adicione `rich_tooltips` ao seu `INSTALLED_APPS` em `settings.py`:**

    Certifique-se de que ele venha *antes* de `django.contrib.admin` se você pretende sobrescrever templates do admin (como `base_site.html`).

    ```python
    # settings.py
    INSTALLED_APPS = [
        # ... outros apps
        'rich_tooltips', # Adicione o app do plugin
        'django.contrib.admin',
        # ... outros apps
    ]
    ```

3.  **Configuração do Template:**
    O plugin depende que arquivos JavaScript e CSS sejam incluídos nas suas páginas do admin. Ele fornece um `templates/admin/base_site.html` que estende o padrão e inclui os arquivos necessários via CDN (para `marked.js`) e arquivos estáticos (para o JS/CSS do plugin).

    *   **Se você NÃO sobrescreve `admin/base_site.html`:** Você não precisa fazer nada, pois o Django pegará automaticamente o template do plugin devido à ordem em `INSTALLED_APPS`.
    *   **Se você SOBRESCREVE `admin/base_site.html`:** Você precisa incluir manualmente os arquivos estáticos necessários no seu `base_site.html` personalizado ou garantir que seu template estenda `rich_tooltips/templates/admin/base_site.html`.

        Adicione o seguinte dentro do seu `<head>` ou blocos apropriados:

        ```html
        {% extends "admin/base_site.html" %} {# Ou sua própria base #}
        {% load static %}

        {% block extrastyle %}
          {{ block.super }}
          <link rel="stylesheet" type="text/css" href="{% static 'rich_tooltips/css/rich_tooltips.css' %}">
        {% endblock %}

        {% block extrahead %}
          {{ block.super }}
          {# Carrega a biblioteca marked.js via CDN #}
          <script src="https://cdn.jsdelivr.net/npm/marked@15.0.11/lib/marked.umd.min.js"></script>
          {# Carrega o JS do plugin com defer #}
          <script src="{% static 'rich_tooltips/js/rich_tooltips.js' %}" defer></script>
        {% endblock %}
        ```

4.  **Coletar Arquivos Estáticos:**
    Execute `python manage.py collectstatic` para garantir que os arquivos estáticos do plugin (`rich_tooltips.js`, `rich_tooltips.css`) sejam coletados no seu `STATIC_ROOT`.

