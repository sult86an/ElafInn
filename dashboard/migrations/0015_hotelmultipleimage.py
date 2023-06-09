# Generated by Django 4.1.5 on 2023-03-18 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_alter_hotellocation_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelMultipleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.hotel', verbose_name='اسم الفندق')),
            ],
        ),
    ]
