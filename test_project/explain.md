# Test Project Directory (`test_project/`)

This directory contains a minimal Django project specifically set up to demonstrate and test the `django-rich-tooltips` plugin during development.

## Contents:

*   **`__init__.py`**: Marks this directory as a Python package (part of the project configuration).
*   **`asgi.py`**: Entry point for ASGI-compatible web servers to serve the project (for asynchronous features, though not heavily used here).
*   **`settings.py`**: Django settings file for the test project. It includes `rich_tooltips` in `INSTALLED_APPS` and configures basic project settings (database, static files, etc.).
*   **`urls.py`**: Root URL configuration for the test project. It includes the default Django admin URLs.
*   **`wsgi.py`**: Entry point for WSGI-compatible web servers to serve the project (standard for synchronous Django deployment).
*   **`manage.py`**: Django's command-line utility for administrative tasks (running the server, applying migrations, running tests, etc.).
*   **`db.sqlite3`**: The SQLite database file used by the test project (created after running `migrate`).
*   **`explain.md`**: This file, explaining the contents of the `test_project` directory.

