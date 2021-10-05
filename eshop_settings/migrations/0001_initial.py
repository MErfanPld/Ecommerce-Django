# Generated by Django 3.2.6 on 2021-08-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
                ('copyright', models.TextField(max_length=1000)),
                ('link_twitter', models.URLField()),
                ('link_facebook', models.URLField()),
                ('link_behance', models.URLField()),
                ('link_globe', models.URLField()),
            ],
        ),
    ]
