# Generated by Django 4.1.3 on 2022-11-16 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Cleaning Date')),
                ('method', models.CharField(choices=[('D', 'Dust'), ('W', 'Wash'), ('P', 'Polish')], default='D', max_length=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.swag')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
