# Generated by Django 3.2 on 2023-07-12 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0018_auto_20230711_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('handheld', 'Handheld'), ('accessories', 'Accessories'), ('games', 'Games'), ('console', 'Console')], max_length=254),
        ),
    ]
