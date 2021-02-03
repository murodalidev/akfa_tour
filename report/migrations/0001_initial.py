# Generated by Django 3.0 on 2021-02-03 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('database', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField(blank=True, default=0, null=True)),
                ('company_offered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.CompanyOffered', verbose_name='Tashkilot')),
            ],
            options={
                'verbose_name_plural': '1. TotalReport',
            },
        ),
        migrations.CreateModel(
            name='ServiceReportReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField(blank=True, default=0.0, null=True)),
                ('company_offered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.CompanyOffered', verbose_name='Tashkilot')),
            ],
            options={
                'verbose_name_plural': '5.3 ServiceReportReg',
            },
        ),
        migrations.CreateModel(
            name='ServiceReportPradVisa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField(blank=True, default=0.0, null=True)),
                ('company_offered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.CompanyOffered', verbose_name='Tashkilot')),
            ],
            options={
                'verbose_name_plural': '5.2 ServiceReportPradVisa',
            },
        ),
        migrations.CreateModel(
            name='ServiceReportMid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField(blank=True, default=0.0, null=True)),
                ('company_offered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.CompanyOffered', verbose_name='Tashkilot')),
            ],
            options={
                'verbose_name_plural': '5.1 ServiceReportMid',
            },
        ),
        migrations.CreateModel(
            name='ServiceReportLicence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField(blank=True, default=0.0, null=True)),
                ('company_offered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.CompanyOffered', verbose_name='Tashkilot')),
            ],
            options={
                'verbose_name_plural': '5.4 ServiceReportLicence',
            },
        ),
        migrations.CreateModel(
            name='HotelReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField(blank=True, default=0.0, null=True)),
                ('company_offered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.CompanyOffered', verbose_name='Tashkilot')),
            ],
            options={
                'verbose_name_plural': '4. HotelReport',
            },
        ),
        migrations.CreateModel(
            name='GuestReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(blank=True, default=0, null=True)),
                ('company_offered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.CompanyOffered', verbose_name='Tashkilot')),
            ],
            options={
                'verbose_name_plural': '3. GuestReport',
            },
        ),
        migrations.CreateModel(
            name='AirTicketReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(blank=True, default=0, null=True)),
                ('company_offered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.CompanyOffered', verbose_name='Tashkilot')),
            ],
            options={
                'verbose_name_plural': '2. AirTicketReport',
            },
        ),
    ]