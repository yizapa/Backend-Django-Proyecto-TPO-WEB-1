# Generated by Django 4.1 on 2023-07-07 14:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("app_solicitud", "0002_alter_solicitud_mensaje_alter_solicitud_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="solicitud",
            name="actualizado",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="solicitud",
            name="hora",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
