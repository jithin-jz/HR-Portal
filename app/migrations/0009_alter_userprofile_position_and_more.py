# Generated by Django 5.1 on 2024-10-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_alter_userprofile_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="position",
            field=models.CharField(
                choices=[
                    ("developer", "Developer"),
                    ("uiux", "UI/UX Designer"),
                    ("manager", "Manager"),
                    ("analyst", "Analyst"),
                ],
                default="developer",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(default="default.jpg", upload_to="profile_pics/"),
        ),
    ]
