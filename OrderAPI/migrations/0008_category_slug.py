# Generated by Django 4.2.7 on 2023-11-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderAPI', '0007_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]