# Desarrollo y Pruebas

Sigue estos pasos para configurar el proyecto para desarrollo o pruebas:

1.  **Clona el Repositorio:**
    ```bash
    git clone https://github.com/yourusername/django-rich-tooltips.git # Reemplaza con la URL real
    cd django-rich-tooltips
    ```

2.  **Configura el Entorno Virtual:**
    Se recomienda encarecidamente usar un entorno virtual.
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3.  **Instala en Modo Editable:**
    Esto instala el paquete de tal manera que los cambios en el código fuente se reflejan inmediatamente sin necesidad de reinstalación.
    ```bash
    pip install -e .
    ```
    Si también quieres instalar dependencias de prueba (si están definidas como un extra en `setup.py`):
    ```bash
    # pip install -e .[test]
    ```

4.  **Navega al Proyecto de Prueba:**
    Se incluye un proyecto Django de ejemplo para fines de prueba.
    ```bash
    cd test_project
    ```

5.  **Aplica las Migraciones:**
    Configura la base de datos para el proyecto de prueba.
    ```bash
    python manage.py migrate
    ```

6.  **Ejecuta las Pruebas:**
    Ejecuta las pruebas unitarias para la app `rich_tooltips`.
    ```bash
    python manage.py test rich_tooltips
    ```

7.  **Crea un Superusuario:**
    Necesitas un usuario administrador para acceder a la interfaz de administración de Django.
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las indicaciones para establecer un nombre de usuario, correo electrónico (opcional) y contraseña.

8.  **Ejecuta el Servidor de Desarrollo:**
    Inicia el servidor de desarrollo de Django.
    ```bash
    python manage.py runserver
    ```
    Por defecto, se ejecuta en `http://127.0.0.1:8000/`.

9.  **Accede a la Interfaz de Administración:**
    Abre tu navegador web y navega a la URL de administración (p. ej., `http://127.0.0.1:8000/admin/`). Inicia sesión con las credenciales de superusuario que creaste.

10. **Prueba el Plugin:**
    Navega a la sección `Rich Tooltips > Tooltip Test Models` dentro de la interfaz de administración para ver el plugin en acción y probar sus características.

