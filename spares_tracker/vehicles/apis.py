from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from spares_tracker.vehicles.models import (
    Country, VehicleModel, Vehicle)
from spares_tracker.vehicles.services import vehicle_create, vehicle_update
from spares_tracker.api.mixins import ApiAuthMixin


class VehicleCreateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        MONTH_CHOICES = (
            (1, 'January'),
            (2, 'February'),
            (3, 'March'),
            (4, 'April'),
            (5, 'May'),
            (6, 'June'),
            (7, 'July'),
            (8, 'August'),
            (9, 'September'),
            (10, 'October'),
            (11, 'November'),
            (12, 'December')
        )

        COLOR_CHOICES = (
            ('BEIGE', 'Beige'),
            ('BLACK', 'Black'),
            ('BLUE', 'Blue'),
            ('BRONZE', 'Bronze'),
            ('BROWN', 'Brown'),
            ('GOLD', 'Gold'),
            ('GRAY', 'Gray'),
            ('GREEN', 'Green'),
            ('MAROON', 'Maroon'),
            ('ORANGE', 'Orange'),
            ('PEARL', 'Pearl'),
            ('PINK', 'Pink'),
            ('PURPLE', 'Purple'),
            ('RED', 'Red'),
            ('SILVER', 'Silver'),
            ('WHITE', 'White'),
            ('YELLOW', 'Yellow'),
            ('UNSPECIFIED', 'Unspecified')
        )

        FUEL_CHOICES = (
            ('PETROL', 'Petrol'),
            ('DIESEL', 'Diesel'),
            ('ELECTRIC', 'Electric'),
            ('HYBRID_DIESEL', 'Hybrid (Diesel)'),
            ('HYBRID_PETROL', 'Hybrid (Petrol)'),
            ('CNG', 'CNG'),
            ('PLG', 'PLG'),
            ('UNSPECIFIED', 'Unspecified')
        )

        number_plate = serializers.CharField(required=True, max_length=20)
        country_of_registration = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
        chasis_number = serializers.CharField(required=True, max_length=255)
        registration_year = serializers.IntegerField(required=True)
        registration_month = serializers.ChoiceField(choices=MONTH_CHOICES, required=True)
        manufacture_year = serializers.IntegerField(required=True)
        manufacture_month = serializers.ChoiceField(choices=MONTH_CHOICES, required=True)
        vehicle_model = serializers.PrimaryKeyRelatedField(queryset=VehicleModel.objects.all())
        vehicle_model_code = serializers.CharField(required=True, max_length=255)
        engine_size = serializers.IntegerField(required=True)
        exterior_color = serializers.ChoiceField(choices=COLOR_CHOICES, required=True)
        fuel = serializers.ChoiceField(choices=FUEL_CHOICES, required=True)
        transmission = serializers.ChoiceField(choices = Vehicle.Transmission.choices ,required=True)
        body_type = serializers.ChoiceField(choices = Vehicle.BodyType.choices ,required=True)
        drive_train = serializers.ChoiceField(choices = Vehicle.DriveTrain.choices ,required=True)
        steering = serializers.ChoiceField(choices = Vehicle.Steering.choices ,required=True)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        vehicle_create(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class VehicleUpdateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        MONTH_CHOICES = (
            (1, 'January'),
            (2, 'February'),
            (3, 'March'),
            (4, 'April'),
            (5, 'May'),
            (6, 'June'),
            (7, 'July'),
            (8, 'August'),
            (9, 'September'),
            (10, 'October'),
            (11, 'November'),
            (12, 'December')
        )

        COLOR_CHOICES = (
            ('BEIGE', 'Beige'),
            ('BLACK', 'Black'),
            ('BLUE', 'Blue'),
            ('BRONZE', 'Bronze'),
            ('BROWN', 'Brown'),
            ('GOLD', 'Gold'),
            ('GRAY', 'Gray'),
            ('GREEN', 'Green'),
            ('MAROON', 'Maroon'),
            ('ORANGE', 'Orange'),
            ('PEARL', 'Pearl'),
            ('PINK', 'Pink'),
            ('PURPLE', 'Purple'),
            ('RED', 'Red'),
            ('SILVER', 'Silver'),
            ('WHITE', 'White'),
            ('YELLOW', 'Yellow'),
            ('UNSPECIFIED', 'Unspecified')
        )

        FUEL_CHOICES = (
            ('PETROL', 'Petrol'),
            ('DIESEL', 'Diesel'),
            ('ELECTRIC', 'Electric'),
            ('HYBRID_DIESEL', 'Hybrid (Diesel)'),
            ('HYBRID_PETROL', 'Hybrid (Petrol)'),
            ('CNG', 'CNG'),
            ('PLG', 'PLG'),
            ('UNSPECIFIED', 'Unspecified')
        )

        number_plate = serializers.CharField(required=True, max_length=20)
        country_of_registration = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
        chasis_number = serializers.CharField(required=True, max_length=255)
        registration_year = serializers.IntegerField(required=True)
        registration_month = serializers.ChoiceField(choices=MONTH_CHOICES, required=True)
        manufacture_year = serializers.IntegerField(required=True)
        manufacture_month = serializers.ChoiceField(choices=MONTH_CHOICES, required=True)
        vehicle_model = serializers.PrimaryKeyRelatedField(queryset=VehicleModel.objects.all())
        vehicle_model_code = serializers.CharField(required=True, max_length=255)
        engine_size = serializers.IntegerField(required=True)
        exterior_color = serializers.ChoiceField(choices=COLOR_CHOICES, required=True)
        fuel = serializers.ChoiceField(choices=FUEL_CHOICES, required=True)
        transmission = serializers.ChoiceField(choices = Vehicle.Transmission.choices ,required=True)
        body_type = serializers.ChoiceField(choices = Vehicle.BodyType.choices ,required=True)
        drive_train = serializers.ChoiceField(choices = Vehicle.DriveTrain.choices ,required=True)
        steering = serializers.ChoiceField(choices = Vehicle.Steering.choices ,required=True)
        vehicle_id = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        vehicle_id = serializer.validated_data['vehicle_id']

        vehicle_update(vehicle_id=vehicle_id, **serializer.validated_data)

        return Response(status=status.HTTP_200_OK)