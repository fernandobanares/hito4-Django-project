# Generated by Django 5.1.2 on 2024-10-23 00:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0003_contact_delete_contactform"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="flan",
            name="flan_uuid",
        ),
        migrations.RemoveField(
            model_name="flan",
            name="slug",
        ),
        migrations.AddField(
            model_name="flan",
            name="rating",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="flan",
            name="image_url",
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name="flan",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name="Comentario",
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
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                (
                    "flan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.flan"
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]