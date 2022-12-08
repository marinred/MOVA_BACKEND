# Generated by Django 4.1.3 on 2022-12-06 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("webtoon", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=30)),
                ("title", models.CharField(max_length=30)),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(max_length=255, null=True, upload_to="media/"),
                ),
                ("count", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "webtoon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webtoon.webtoon",
                    ),
                ),
            ],
        ),
    ]