# Generated by Django 3.2 on 2023-07-11 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0017_auto_20230711_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('games', 'Games'), ('handheld', 'Handheld'), ('console', 'Console'), ('accessories', 'Accessories')], max_length=254),
        ),
        migrations.AlterField(
            model_name='selltous',
            name='description',
            field=models.TextField(max_length=254),
        ),
    ]
