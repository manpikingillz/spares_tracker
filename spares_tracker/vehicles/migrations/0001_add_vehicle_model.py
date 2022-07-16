# Generated by Django 3.2.13 on 2022-07-16 03:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_make_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_model_name', models.CharField(max_length=255)),
                ('vehicle_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_models', to='vehicles.vehiclemake')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chasis_number', models.CharField(max_length=255)),
                ('registration_year', models.SmallIntegerField()),
                ('registration_month', models.SmallIntegerField()),
                ('manufacture_year', models.SmallIntegerField()),
                ('manufacture_month', models.SmallIntegerField()),
                ('vehicle_model_code', models.CharField(max_length=255)),
                ('engine_size', models.SmallIntegerField()),
                ('exterior_color', models.CharField(max_length=10)),
                ('fuel', models.CharField(max_length=10)),
                ('transmission', models.CharField(max_length=50)),
                ('body_type', models.CharField(max_length=50)),
                ('country_of_registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='vehicles.country')),
                ('vehicle_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='vehicles.vehiclemodel')),
            ],
        ),
        migrations.AddConstraint(
            model_name='vehicle',
            constraint=models.CheckConstraint(check=models.Q(('registration_year__gte', 1980), ('registration_year__lte', 2022)), name='registration_year_between_1980_and_current_year'),
        ),
        migrations.AddConstraint(
            model_name='vehicle',
            constraint=models.CheckConstraint(check=models.Q(('registration_month__gte', 1), ('registration_month__lte', 12)), name='registration_month_between_1_and_12'),
        ),
        migrations.AddConstraint(
            model_name='vehicle',
            constraint=models.CheckConstraint(check=models.Q(('manufacture_year__gte', 1980), ('manufacture_year__lte', 2022)), name='manufacture_year_between_1980_and_current_year'),
        ),
        migrations.AddConstraint(
            model_name='vehicle',
            constraint=models.CheckConstraint(check=models.Q(('manufacture_month__gte', 1), ('manufacture_month__lte', 12)), name='manufacture_month_between_1_and_12'),
        ),
    ]
