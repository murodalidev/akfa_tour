# Generated by Django 3.0 on 2021-02-03 12:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestinfo',
            name='created_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Sana'),
        ),
    ]
