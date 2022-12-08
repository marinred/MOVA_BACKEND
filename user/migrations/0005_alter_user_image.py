# Generated by Django 4.1.3 on 2022-12-08 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_alter_user_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(
                default="basicprofileimage.png",
                max_length=255,
                null=True,
                upload_to="user/",
            ),
        ),
    ]