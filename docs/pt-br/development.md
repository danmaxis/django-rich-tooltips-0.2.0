# Desenvolvimento & Testes

Siga estes passos para configurar o projeto para desenvolvimento ou testes:

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/yourusername/django-rich-tooltips.git # Substitua pela URL real
    cd django-rich-tooltips
    ```

2.  **Configure o Ambiente Virtual:**
    É altamente recomendável usar um ambiente virtual.
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3.  **Instale em Modo Editável:**
    Isso instala o pacote de forma que as alterações no código-fonte sejam refletidas imediatamente sem necessidade de reinstalação.
    ```bash
    pip install -e .
    ```
    Se você também quiser instalar dependências de teste (se definidas como um extra em `setup.py`):
    ```bash
    # pip install -e .[test]
    ```

4.  **Navegue até o Projeto de Teste:**
    Um projeto Django de exemplo está incluído para fins de teste.
    ```bash
    cd test_project
    ```

5.  **Aplique as Migrações:**
    Configure o banco de dados para o projeto de teste.
    ```bash
    python manage.py migrate
    ```

6.  **Execute os Testes:**
    Execute os testes unitários para o app `rich_tooltips`.
    ```bash
    python manage.py test rich_tooltips
    ```

7.  **Crie um Superusuário:**
    Você precisa de um usuário administrador para acessar a interface de administração do Django.
    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções para definir um nome de usuário, email (opcional) e senha.

8.  **Execute o Servidor de Desenvolvimento:**
    Inicie o servidor de desenvolvimento do Django.
    ```bash
    python manage.py runserver
    ```
    Por padrão, ele roda em `http://127.0.0.1:8000/`.

9.  **Acesse a Interface de Administração:**
    Abra seu navegador e navegue até a URL do admin (por exemplo, `http://127.0.0.1:8000/admin/`). Faça login com as credenciais de superusuário que você criou.

10. **Teste o Plugin:**
    Navegue até a seção `Rich Tooltips > Tooltip Test Models` dentro da interface de administração para ver o plugin em ação e testar suas funcionalidades.

