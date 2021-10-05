# Generated by Django 3.2.6 on 2021-10-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0003_setting_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='setting',
            name='copy_right',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='setting',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]