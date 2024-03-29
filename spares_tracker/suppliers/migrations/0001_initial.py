# Generated by Django 3.2.13 on 2022-08-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
