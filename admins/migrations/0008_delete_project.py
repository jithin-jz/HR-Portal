# Generated by Django 5.1 on 2024-11-30 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("admins", "0007_project"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Project",
        ),
    ]