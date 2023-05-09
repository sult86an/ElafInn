# Generated by Django 4.1.5 on 2023-03-18 14:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_hotellocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotellocation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotellocation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]