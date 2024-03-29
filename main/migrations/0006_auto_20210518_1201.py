# Generated by Django 3.1 on 2021-05-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210518_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('title',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=1, max_length=20, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
