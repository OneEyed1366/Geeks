# Generated by Django 3.2.4 on 2021-07-09 09:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0009_alter_user_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 11, 9, 35, 34, 285209, tzinfo=utc)),
        ),
    ]