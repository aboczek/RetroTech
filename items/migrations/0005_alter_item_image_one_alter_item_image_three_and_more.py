# Generated by Django 4.2.1 on 2023-06-23 16:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_rename_image_item_image_one_item_image_three_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image_one',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_three',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_two',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='image'),
        ),
    ]
