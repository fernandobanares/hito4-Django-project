# Generated by Django 5.1.2 on 2024-10-25 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0007_alter_comentario_flan"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flan",
            name="image_url",
            field=models.CharField(max_length=500),
        ),
    ]