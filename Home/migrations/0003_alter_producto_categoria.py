# Generated by Django 5.0 on 2023-12-05 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_rename_producto_carrito_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Coffee', 'coffee'), ('bakery', 'pattisierie')], max_length=50),
        ),
    ]