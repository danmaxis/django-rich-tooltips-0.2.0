# Développement & Tests

Suivez ces étapes pour configurer le projet pour le développement ou les tests :

1.  **Clonez le Dépôt :**
    ```bash
    git clone https://github.com/yourusername/django-rich-tooltips.git # Remplacez par l'URL réelle
    cd django-rich-tooltips
    ```

2.  **Configurez l'Environnement Virtuel :**
    Il est fortement recommandé d'utiliser un environnement virtuel.
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sous Windows, utilisez `venv\Scripts\activate`
    ```

3.  **Installez en Mode Éditable :**
    Ceci installe le paquet de telle sorte que les modifications dans le code source sont immédiatement reflétées sans nécessiter de réinstallation.
    ```bash
    pip install -e .
    ```
    Si vous souhaitez également installer les dépendances de test (si définies comme un extra dans `setup.py`) :
    ```bash
    # pip install -e .[test]
    ```

4.  **Naviguez vers le Projet de Test :**
    Un projet Django d'exemple est inclus à des fins de test.
    ```bash
    cd test_project
    ```

5.  **Appliquez les Migrations :**
    Configurez la base de données pour le projet de test.
    ```bash
    python manage.py migrate
    ```

6.  **Exécutez les Tests :**
    Exécutez les tests unitaires pour l'application `rich_tooltips`.
    ```bash
    python manage.py test rich_tooltips
    ```

7.  **Créez un Superutilisateur :**
    Vous avez besoin d'un utilisateur administrateur pour accéder à l'interface d'administration de Django.
    ```bash
    python manage.py createsuperuser
    ```
    Suivez les invites pour définir un nom d'utilisateur, un email (facultatif) et un mot de passe.

8.  **Exécutez le Serveur de Développement :**
    Démarrez le serveur de développement Django.
    ```bash
    python manage.py runserver
    ```
    Par défaut, il s'exécute sur `http://127.0.0.1:8000/`.

9.  **Accédez à l'Interface d'Administration :**
    Ouvrez votre navigateur web et naviguez vers l'URL d'administration (par exemple, `http://127.0.0.1:8000/admin/`). Connectez-vous avec les identifiants de superutilisateur que vous avez créés.

10. **Testez le Plugin :**
    Naviguez vers la section `Rich Tooltips > Tooltip Test Models` dans l'interface d'administration pour voir le plugin en action et tester ses fonctionnalités.

