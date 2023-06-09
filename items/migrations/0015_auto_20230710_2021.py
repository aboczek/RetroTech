# Generated by Django 3.2 on 2023-07-10 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0014_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('games', 'Games'), ('console', 'Console'), ('accessories', 'Accessories'), ('handheld', 'Handheld')], max_length=254),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.category'),
        ),
    ]
