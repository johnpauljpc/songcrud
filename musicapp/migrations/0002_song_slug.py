# Generated by Django 4.0.6 on 2022-11-04 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.SlugField(default='admin'),
            preserve_default=False,
        ),
    ]