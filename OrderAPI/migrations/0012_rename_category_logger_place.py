# Generated by Django 4.2.7 on 2023-11-28 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderAPI', '0011_place_logger_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logger',
            old_name='category',
            new_name='place',
        ),
    ]
