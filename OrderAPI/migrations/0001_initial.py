# Generated by Django 4.2.7 on 2023-11-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField(max_length=12)),
                ('address', models.TextField()),
                ('order_time', models.DateField(auto_now=True)),
            ],
        ),
    ]
