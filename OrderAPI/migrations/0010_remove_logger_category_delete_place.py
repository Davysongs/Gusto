# Generated by Django 4.2.7 on 2023-11-27 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderAPI', '0009_rename_category_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logger',
            name='category',
        ),
        migrations.DeleteModel(
            name='Place',
        ),
    ]
