# Generated by Django 3.2.6 on 2021-08-31 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_about', '0002_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='image',
            new_name='person_image',
        ),
    ]
