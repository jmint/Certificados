# Generated by Django 2.2 on 2020-10-13 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserFiles', '0002_auto_20200621_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='estado',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='files',
            name='tipo_doc',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='files',
            name='tipo_inspeccion',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
