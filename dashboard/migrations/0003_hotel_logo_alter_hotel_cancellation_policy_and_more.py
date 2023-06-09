# Generated by Django 4.1.5 on 2023-03-16 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_hotel_nationality'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/gallery/'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='Cancellation_policy',
            field=models.IntegerField(blank=True, choices=[(1, 'مستردة'), (2, 'غير مستردة')], null=True, verbose_name='سياسة الإلغاء'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='category',
            field=models.IntegerField(choices=[(1, 'نجمة'), (2, 'نجمتان'), (3, '3 نجوم'), (4, '4 نجوم'), (5, '5 نجوم'), (6, 'شقق مخدومة'), (7, 'غير مصنف')], verbose_name='التصنيف'),
        ),
    ]
