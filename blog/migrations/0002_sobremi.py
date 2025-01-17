# Generated by Django 4.2.16 on 2024-12-26 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SobreMi",
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
                ("texto", models.TextField()),
                (
                    "imagen",
                    models.ImageField(blank=True, null=True, upload_to="about/"),
                ),
                ("ultima_actualizacion", models.DateTimeField(auto_now=True)),
            ],
            options={"verbose_name": "Sobre Mí", "verbose_name_plural": "Sobre Mí",},
        ),
    ]
