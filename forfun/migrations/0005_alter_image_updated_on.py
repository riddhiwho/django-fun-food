# Generated by Django 4.0.3 on 2022-03-19 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forfun', '0004_image_kid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
