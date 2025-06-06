# Generated by Django 5.2 on 2025-04-29 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TooltipTestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(help_text='This field will have a basic HTML tooltip.')),
                ('markdown_field', models.TextField(blank=True, help_text='This field will have a Markdown tooltip (requires JS library).')),
            ],
        ),
    ]
