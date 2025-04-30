# Entwicklung & Testen

Befolgen Sie diese Schritte, um das Projekt für die Entwicklung oder das Testen einzurichten:

1.  **Klonen Sie das Repository:**
    ```bash
    git clone https://github.com/yourusername/django-rich-tooltips.git # Ersetzen Sie dies durch die tatsächliche URL
    cd django-rich-tooltips
    ```

2.  **Richten Sie eine virtuelle Umgebung ein:**
    Es wird dringend empfohlen, eine virtuelle Umgebung zu verwenden.
    ```bash
    python -m venv venv
    source venv/bin/activate  # Unter Windows verwenden Sie `venv\Scripts\activate`
    ```

3.  **Installieren Sie im bearbeitbaren Modus:**
    Dies installiert das Paket so, dass Änderungen im Quellcode sofort wirksam werden, ohne dass eine Neuinstallation erforderlich ist.
    ```bash
    pip install -e .
    ```
    Wenn Sie auch Testabhängigkeiten installieren möchten (falls als Extra in `setup.py` definiert):
    ```bash
    # pip install -e .[test]
    ```

4.  **Navigieren Sie zum Testprojekt:**
    Ein Beispiel-Django-Projekt ist zu Testzwecken enthalten.
    ```bash
    cd test_project
    ```

5.  **Wenden Sie Migrationen an:**
    Richten Sie die Datenbank für das Testprojekt ein.
    ```bash
    python manage.py migrate
    ```

6.  **Führen Sie Tests aus:**
    Führen Sie die Unit-Tests für die `rich_tooltips`-App aus.
    ```bash
    python manage.py test rich_tooltips
    ```

7.  **Erstellen Sie einen Superuser:**
    Sie benötigen einen Admin-Benutzer, um auf die Django-Admin-Oberfläche zugreifen zu können.
    ```bash
    python manage.py createsuperuser
    ```
    Folgen Sie den Anweisungen, um einen Benutzernamen, eine E-Mail-Adresse (optional) und ein Passwort festzulegen.

8.  **Führen Sie den Entwicklungsserver aus:**
    Starten Sie den Django-Entwicklungsserver.
    ```bash
    python manage.py runserver
    ```
    Standardmäßig läuft er auf `http://127.0.0.1:8000/`.

9.  **Greifen Sie auf die Admin-Oberfläche zu:**
    Öffnen Sie Ihren Webbrowser und navigieren Sie zur Admin-URL (z. B. `http://127.0.0.1:8000/admin/`). Melden Sie sich mit den von Ihnen erstellten Superuser-Anmeldeinformationen an.

10. **Testen Sie das Plugin:**
    Navigieren Sie zum Abschnitt `Rich Tooltips > Tooltip Test Models` in der Admin-Oberfläche, um das Plugin in Aktion zu sehen und seine Funktionen zu testen.

