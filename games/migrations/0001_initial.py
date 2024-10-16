# Generated by Django 5.1.1 on 2024-10-11 05:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="GameTracking",
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
                (
                    "game_type",
                    models.CharField(
                        choices=[
                            ("math_facts", "Math Facts Practice"),
                            ("anagram_hunt", "Anagram Hunt"),
                        ],
                        max_length=20,
                    ),
                ),
                ("game_settings", models.JSONField()),
                ("score", models.IntegerField(blank=True, null=True)),
                ("tries", models.IntegerField(default=0)),
                ("start_time", models.DateTimeField(auto_now_add=True)),
                ("end_time", models.DateTimeField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
