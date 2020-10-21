# Generated by Django 2.2 on 2020-06-17 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('cod_file', models.AutoField(max_length=8, primary_key=True, serialize=False)),
                ('name_file', models.CharField(blank=True, max_length=100, null=True)),
                ('url_file', models.CharField(blank=True, max_length=150, null=True)),
                ('cod_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'files',
            },
        ),
    ]
