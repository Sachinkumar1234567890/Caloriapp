# Generated by Django 5.0 on 2024-02-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calapp', '0006_alter_dailycalory_dfoodimg_alter_foodmodel_foodimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailycalory',
            name='dfoodimg',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='foodmodel',
            name='foodimg',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
