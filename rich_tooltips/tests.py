# -*- coding: utf-8 -*-
from django.test import TestCase, RequestFactory
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model

from html.parser import HTMLParser
import html

from .models import TooltipTestModel
from .admin import TooltipTestModelAdmin

User = get_user_model()

class RichTooltipsModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create test data once for all test methods
        cls.user = User.objects.create_superuser("admin_test", "" , "password")
        cls.test_obj = TooltipTestModel.objects.create(
            name="Test Model",
            description="This is a test description.",
            markdown_field="*Markdown content*"
        )


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
        # Check that the HTML tooltip is set correctly
        tooltip_html_attribute = html.unescape(form_instance.fields["description"].widget.attrs["data-tooltip-html"])

        self.assertEqual(
            tooltip_html_attribute,
            self.test_obj.tooltip_content_html
        )

        # Check markdown_field widget attributes
        self.assertIn("data-tooltip-markdown", form_instance.fields["markdown_field"].widget.attrs)
        tooltip_markdown_attribute = html.unescape(form_instance.fields["markdown_field"].widget.attrs["data-tooltip-markdown"])
        self.assertEqual(
            tooltip_markdown_attribute,
            self.test_obj.tooltip_content_markdown
        )
    def test_admin_list_display_tooltip(self):
        """Test the custom list display field with tooltip."""
        request = self.factory.get("/admin/rich_tooltips/tooltiptestmodel/")
        request.user = self.user
        # Note: Testing the actual rendered HTML output of the list display usually requires
        # a full client request or more complex template rendering tests.
        # Here, we just test the method that generates the HTML.
        output_html = html.unescape(self.model_admin.description_with_tooltip(self.test_obj))
        # Remove all HTML tags for easier assertion
        tag_stripped_html = extract_all_text(output_html)
        self.assertIn("data-tooltip-html", output_html)
        # Display the tooltip content
        self.assertIn("This is an  HTML  tooltip defined in the model!", tag_stripped_html)
        self.assertIn(self.test_obj.description, output_html)

# Note: Testing the JavaScript functionality (frontend) typically requires
# different tools like Selenium or Django's StaticLiveServerTestCase, which
# are more complex to set up and run in this environment. These tests focus
# on the backend integration.



class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []

    def handle_data(self, data):
        self.result.append(data)

    def handle_starttag(self, tag, attrs):
        for attr_name, attr_value in attrs:
            if attr_name in ("alt", "title", "placeholder", "aria-label", "data-tooltip-html", "data-tooltip-markdown"):
                self.result.append(attr_value)

    def get_data(self):
        return ' '.join(self.result)

def extract_all_text(html_string):
    parser = TextExtractor()
    parser.feed(html.unescape(html_string))
    fst = parser.get_data()
    # Feed again to handle any nested tags
    parser2 = TextExtractor()
    # Remove double spaces in fst
    fst = ' '.join([x.strip() for x in fst.split()])
    parser2.feed(fst)
    return parser2.get_data()
