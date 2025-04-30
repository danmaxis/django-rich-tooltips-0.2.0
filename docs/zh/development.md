# 开发与测试

请按照以下步骤设置项目以进行开发或测试：

1.  **克隆存储库：**
    ```bash
    git clone https://github.com/yourusername/django-rich-tooltips.git # 替换为实际 URL
    cd django-rich-tooltips
    ```

2.  **设置虚拟环境：**
    强烈建议使用虚拟环境。
    ```bash
    python -m venv venv
    source venv/bin/activate  # 在 Windows 上使用 `venv\Scripts\activate`
    ```

3.  **以可编辑模式安装：**
    这将安装软件包，使得源代码中的更改能够立即反映出来，而无需重新安装。
    ```bash
    pip install -e .
    ```
    如果您还想安装测试依赖项（如果在 `setup.py` 中定义为 extra）：
    ```bash
    # pip install -e .[test]
    ```

4.  **导航到测试项目：**
    包含一个示例 Django 项目用于测试目的。
    ```bash
    cd test_project
    ```

5.  **应用迁移：**
    为测试项目设置数据库。
    ```bash
    python manage.py migrate
    ```

6.  **运行测试：**
    为 `rich_tooltips` 应用程序执行单元测试。
    ```bash
    python manage.py test rich_tooltips
    ```

7.  **创建超级用户：**
    您需要一个管理员用户才能访问 Django 管理界面。
    ```bash
    python manage.py createsuperuser
    ```
    按照提示设置用户名、电子邮件（可选）和密码。

8.  **运行开发服务器：**
    启动 Django 开发服务器。
    ```bash
    python manage.py runserver
    ```
    默认情况下，它在 `http://127.0.0.1:8000/` 上运行。

9.  **访问管理界面：**
    打开您的网络浏览器并导航到管理 URL（例如，`http://127.0.0.1:8000/admin/`）。使用您创建的超级用户凭据登录。

10. **测试插件：**
    导航到管理界面中的 `Rich Tooltips > Tooltip Test Models` 部分，以查看插件的实际运行情况并测试其功能。

