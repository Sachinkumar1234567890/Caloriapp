# Generated by Django 5.0.7 on 2024-07-31 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calapp', '0013_rename_register_user_register'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_register',
        ),
    ]
