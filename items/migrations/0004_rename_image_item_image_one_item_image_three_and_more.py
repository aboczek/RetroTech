# Generated by Django 4.2.1 on 2023-06-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_category_options_alter_item_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='image_one',
        ),
        migrations.AddField(
            model_name='item',
            name='image_three',
            field=models.ImageField(blank=True, default='placeholder', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image_two',
            field=models.ImageField(blank=True, default='placeholder', null=True, upload_to=''),
        ),
    ]
