# Generated by Django 4.0.2 on 2022-03-02 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
    ]
