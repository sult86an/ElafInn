# Generated by Django 4.1.5 on 2023-03-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_alter_hotelmultipleimage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelmultipleimage',
            name='images',
            field=models.FileField(upload_to='images/hotel_images'),
        ),
    ]