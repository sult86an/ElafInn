# Generated by Django 4.1.5 on 2023-03-18 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_hotel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]