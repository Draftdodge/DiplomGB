# Generated by Django 5.0.4 on 2024-04-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkings', '0003_order_parking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]