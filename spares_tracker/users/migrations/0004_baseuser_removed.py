# Generated by Django 3.2.13 on 2022-07-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_baseuser_jwt_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='removed',
            field=models.BooleanField(default=False),
        ),
    ]