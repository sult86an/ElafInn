# Generated by Django 4.1.5 on 2023-03-23 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0020_alter_roomtype_capacity_alter_roomtype_roomtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomNo', models.CharField(blank=True, max_length=250, null=True, verbose_name='رقم الغرفة')),
                ('capacity', models.IntegerField(blank=True, default=1, verbose_name='عدد استيعاب الغرفة للأشخاص من هذا النوع')),
                ('Electric', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'تلفزيون'), ('2', 'فرن'), ('3', 'ميكرويف'), ('4', 'غسالة'), ('5', 'مكواة'), ('6', 'غلاية شاهي'), ('7', 'ثلاجة')], max_length=10, null=True, verbose_name='الأجهزة الكهربائية')),
                ('Facilities', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'مطبخ'), ('2', 'غرفة غسيل'), ('3', 'بانيو/ جاكوزي')], max_length=10, null=True, verbose_name='المرافق')),
                ('Services', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'واي فاي'), ('2', 'خدمة الغسيل'), ('3', 'خدمة الغرف')], max_length=10, null=True, verbose_name='الخدمات المجانية')),
                ('is_active', models.BooleanField(default=False, verbose_name='تفعيل الغرفة')),
                ('status', models.IntegerField(blank=True, choices=[('1', 'غير مفعلة'), ('2', 'متاحة'), ('3', 'انتظار'), ('4', 'محجوزة')], default=1, max_length=250, verbose_name='حالة الغرفة')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='مالك الغرفة')),
                ('roomType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.roomtype', verbose_name='نوع الغرفة')),
            ],
        ),
    ]