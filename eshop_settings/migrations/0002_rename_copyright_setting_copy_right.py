# Generated by Django 3.2.6 on 2021-08-22 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='copyright',
            new_name='copy_right',
        ),
    ]