# Generated by Django 4.0.3 on 2022-03-17 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forfun', '0002_alter_image_food_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='kid_age',
            field=models.IntegerField(),
        ),
    ]
