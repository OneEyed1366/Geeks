# Generated by Django 3.2.4 on 2021-07-09 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
