# Generated by Django 4.1.3 on 2022-11-17 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cleaning'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cleaning',
            old_name='item',
            new_name='swag',
        ),
    ]
