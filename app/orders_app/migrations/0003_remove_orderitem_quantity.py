# Generated by Django 3.2.4 on 2021-07-09 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders_app', '0002_alter_orderitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity',
        ),
    ]
