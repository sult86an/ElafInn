# Generated by Django 4.1.5 on 2023-03-23 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0033_alter_room_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_view',
            field=models.BooleanField(default=False, verbose_name='مطلة؟'),
        ),
    ]