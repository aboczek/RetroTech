# Generated by Django 3.2 on 2023-07-10 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0015_auto_20230710_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('games', 'Games'), ('handheld', 'Handheld'), ('console', 'Console'), ('accessories', 'Accessories')], max_length=254),
        ),
    ]
