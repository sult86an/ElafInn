# Generated by Django 4.1.5 on 2023-04-04 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0042_annualrent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualrent',
            name='rooms',
            field=models.ManyToManyField(limit_choices_to={'room__roomType__hotel__slug': 'hotel-slug'}, to='dashboard.room', verbose_name='الغرف'),
        ),
    ]
