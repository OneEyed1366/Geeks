# Generated by Django 3.1 on 2021-05-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(verbose_name='возраст'),
        ),
    ]