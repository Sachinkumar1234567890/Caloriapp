# Generated by Django 5.0 on 2024-01-31 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calapp', '0002_foodmodel_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodmodel',
            old_name='img',
            new_name='foodimg',
        ),
    ]
