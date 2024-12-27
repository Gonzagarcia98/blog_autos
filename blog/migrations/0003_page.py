# Generated by Django 4.2.16 on 2024-12-26 22:51

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0002_sobremi"),
    ]

    operations = [
        migrations.CreateModel(
            name="Page",
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
                ("titulo", models.CharField(max_length=200)),
                ("subtitulo", models.CharField(max_length=200)),
                ("contenido", ckeditor.fields.RichTextField()),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                (
                    "imagen",
                    models.ImageField(blank=True, null=True, upload_to="pages/"),
                ),
                (
                    "autor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-fecha_creacion"],},
        ),
    ]