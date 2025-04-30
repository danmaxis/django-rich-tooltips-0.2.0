from rich_tooltips.models import TooltipTestModel

# Check if data already exists to avoid duplicates
if not TooltipTestModel.objects.filter(name='Test Item 1').exists():
    TooltipTestModel.objects.create(
        name='Test Item 1',
        description='This is a test item with tooltips.',
        markdown_field='Another test field.'
    )
    print("Test data created.")
else:
    print("Test data already exists.")

