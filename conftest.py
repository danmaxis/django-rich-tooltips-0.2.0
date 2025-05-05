import os
import django
from django.conf import settings
from django.core.management import call_command


# Setup Django before pytest runs
def pytest_configure():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rich_tooltips.test_settings")
    django.setup()
    # Run migrations for the test database
    call_command("migrate")