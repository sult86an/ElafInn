# Generated by Django 4.1.5 on 2023-03-23 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0035_season_alter_room_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=250, verbose_name='السعر')),
                ('roomType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.roomtype', verbose_name='نوع الغرفة')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.season', verbose_name='الموسم')),
            ],
        ),
    ]
