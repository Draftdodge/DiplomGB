# Generated by Django 5.0.4 on 2024-04-22 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('phone', models.CharField(max_length=20)),
                ('car_number', models.CharField(max_length=9)),
                ('key_number', models.IntegerField(default=0)),
                ('added_at', models.DateField(auto_now=True)),
                ('access', models.BooleanField(default=False)),
                ('phone_access', models.BooleanField(default=False)),
                ('key_access', models.BooleanField(default=False)),
                ('start_access_date', models.DateField(auto_now=True)),
                ('end_access_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('number_of_spot', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('scheme', models.ImageField(null=True, upload_to='')),
                ('reg_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSpots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_spot', models.IntegerField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('occupied', models.BooleanField(default=False)),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkings.parking')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_access_date', models.DateField(auto_now=True)),
                ('end_access_date', models.DateField()),
                ('payment', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkings.client')),
                ('parking_spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkings.parkingspots')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='parking_spot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkings.parkingspots'),
        ),
    ]
