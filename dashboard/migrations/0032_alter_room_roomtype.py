# Generated by Django 4.1.5 on 2023-03-23 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0031_alter_room_roomtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='roomType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.roomtype', verbose_name='نوع الغرفة'),
            preserve_default=False,
        ),
    ]