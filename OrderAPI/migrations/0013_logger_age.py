# Generated by Django 4.2.7 on 2023-11-28 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderAPI', '0012_rename_category_logger_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='logger',
            name='age',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
