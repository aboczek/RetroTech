# Generated by Django 3.2 on 2023-07-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('handheld', 'Handheld'), ('console', 'Console'), ('accessories', 'Accessories'), ('games', 'Games')], max_length=254),
        ),
    ]
