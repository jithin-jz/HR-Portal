# Generated by Django 5.1 on 2024-10-16 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_alter_userprofile_position_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(default="man.png", upload_to="profile_pics/"),
        ),
    ]
