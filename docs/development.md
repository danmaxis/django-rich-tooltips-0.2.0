# Development & Testing

Follow these steps to set up the project for development or testing:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/django-rich-tooltips.git # Replace with actual URL
    cd django-rich-tooltips
    ```

2.  **Set Up Virtual Environment:**
    It is highly recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install in Editable Mode:**
    This installs the package such that changes in the source code are immediately reflected without needing reinstallation.
    ```bash
    pip install -e .
    ```
    If you also want to install testing dependencies (if defined as an extra in `setup.py`):
    ```bash
    # pip install -e .[test]
    ```

4.  **Navigate to Test Project:**
    A sample Django project is included for testing purposes.
    ```bash
    cd test_project
    ```

5.  **Apply Migrations:**
    Set up the database for the test project.
    ```bash
    python manage.py migrate
    ```

6.  **Run Tests:**
    Execute the unit tests for the `rich_tooltips` app.
    ```bash
    python manage.py test rich_tooltips
    ```

7.  **Create Superuser:**
    You need an admin user to access the Django admin interface.
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set a username, email (optional), and password.

8.  **Run Development Server:**
    Start the Django development server.
    ```bash
    python manage.py runserver
    ```
    By default, it runs on `http://127.0.0.1:8000/`.

9.  **Access Admin Interface:**
    Open your web browser and navigate to the admin URL (e.g., `http://127.0.0.1:8000/admin/`). Log in with the superuser credentials you created.

10. **Test the Plugin:**
    Navigate to the `Rich Tooltips > Tooltip Test Models` section within the admin interface to see the plugin in action and test its features.

