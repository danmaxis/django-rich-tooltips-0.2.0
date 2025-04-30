# -*- coding: utf-8 -*-
from django.test import TestCase, RequestFactory
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model

from .models import TooltipTestModel
from .admin import TooltipTestModelAdmin

User = get_user_model()

class RichTooltipsModelTests(TestCase):

    def test_create_tooltip_test_model(self):
        """Test creating an instance of TooltipTestModel."""
        name = "Test Model Instance"
        description = "Description for testing."
        markdown = "# Markdown Content"
        obj = TooltipTestModel.objects.create(
            name=name,
            description=description,
            markdown_field=markdown
        )
        self.assertEqual(obj.name, name)
        self.assertEqual(obj.description, description)
        self.assertEqual(obj.markdown_field, markdown)
        self.assertIn("HTML", obj.tooltip_content_html) # Check default content
        self.assertIn("Markdown", obj.tooltip_content_markdown) # Check default content
        self.assertEqual(str(obj), name)

class RichTooltipsAdminTests(TestCase):

    def setUp(self):
        self.site = AdminSite()
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser("admin_test", "admin@test.com", "password")
        self.model_admin = TooltipTestModelAdmin(TooltipTestModel, self.site)
        self.test_obj = TooltipTestModel.objects.create(
            name="Admin Test",
            description="Testing admin form.",
            markdown_field="*Admin Markdown*"
        )

    def test_admin_form_adds_data_attributes(self):
        """Test that the admin form correctly adds data-tooltip attributes."""
        request = self.factory.get("/admin/rich_tooltips/tooltiptestmodel/{}/change/".format(self.test_obj.pk))
        request.user = self.user # Simulate logged-in superuser

        # Get the form instance used by the admin
        form_class = self.model_admin.get_form(request, obj=self.test_obj)
        form_instance = form_class(instance=self.test_obj)

        # Check description field widget attributes
        self.assertIn("data-tooltip-html", form_instance.fields["description"].widget.attrs)
        self.assertEqual(
            form_instance.fields["description"].widget.attrs["data-tooltip-html"],
            self.test_obj.tooltip_content_html
        )

        # Check markdown_field widget attributes
        self.assertIn("data-tooltip-markdown", form_instance.fields["markdown_field"].widget.attrs)
        self.assertEqual(
            form_instance.fields["markdown_field"].widget.attrs["data-tooltip-markdown"],
            self.test_obj.tooltip_content_markdown
        )
        # Also check the placeholder HTML tooltip added before markdown integration
        self.assertIn("data-tooltip-html", form_instance.fields["markdown_field"].widget.attrs)
        self.assertIn("Markdown content will be rendered here", form_instance.fields["markdown_field"].widget.attrs["data-tooltip-html"])

    def test_admin_list_display_tooltip(self):
        """Test the custom list display field with tooltip."""
        request = self.factory.get("/admin/rich_tooltips/tooltiptestmodel/")
        request.user = self.user
        # Note: Testing the actual rendered HTML output of the list display usually requires
        # a full client request or more complex template rendering tests.
        # Here, we just test the method that generates the HTML.
        output_html = self.model_admin.description_with_tooltip(self.test_obj)
        self.assertIn("data-tooltip-html", output_html)
        self.assertIn("Simple tooltip for description", output_html)
        self.assertIn(self.test_obj.description, output_html)

# Note: Testing the JavaScript functionality (frontend) typically requires
# different tools like Selenium or Django's StaticLiveServerTestCase, which
# are more complex to set up and run in this environment. These tests focus
# on the backend integration.

