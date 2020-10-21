# Generated by Django 2.2 on 2020-06-17 05:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth_user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='auth_user',
            name='key_expires',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 6, 17, 5, 31, 29, 77658, tzinfo=utc), null=True),
        ),
    ]