# Generated by Django 3.1 on 2021-05-18 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart_app', '0002_shoppingcarttax'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingcarttax',
            options={'ordering': ('price',), 'verbose_name': 'Доставка', 'verbose_name_plural': 'Стоимость доставки'},
        ),
        migrations.AddField(
            model_name='shoppingcarttax',
            name='title',
            field=models.CharField(default='to all', max_length=200),
            preserve_default=False,
        ),
    ]
