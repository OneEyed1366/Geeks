# Generated by Django 3.1 on 2021-05-18 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCartTax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(max_length=10, verbose_name='Стоимость доставки')),
            ],
        ),
    ]