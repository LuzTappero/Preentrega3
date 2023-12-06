# Generated by Django 5.0 on 2023-12-05 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_remove_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=255)),
                ('password', models.TextField()),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.user')),
            ],
        ),
    ]
