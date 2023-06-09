# Generated by Django 4.1.5 on 2023-03-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0034_room_is_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=250, verbose_name='الموسم')),
                ('startDate', models.DateField(verbose_name='بداية الموسم')),
                ('endDate', models.DateField(verbose_name='نهاية الموسم')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='room',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'غير مفعلة'), (2, 'متاحة'), (3, 'انتظار'), (4, 'محجوزة')], default=2, verbose_name='حالة الغرفة'),
        ),
    ]
