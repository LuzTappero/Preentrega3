# Generated by Django 5.0 on 2023-12-05 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_producto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
    ]