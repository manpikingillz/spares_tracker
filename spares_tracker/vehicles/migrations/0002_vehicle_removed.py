# Generated by Django 3.2.13 on 2022-07-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_add_vehicle_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='removed',
            field=models.BooleanField(default=False),
        ),
    ]
