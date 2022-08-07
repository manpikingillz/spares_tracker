from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from spares_tracker.vehicles.models import (
    VehicleMake, VehicleModel, Vehicle)
from spares_tracker.vehicles.services import vehicle_create, vehicle_update, vehicle_delete
from spares_tracker.vehicles.selectors import vehicle_detail, vehicle_list, vehicle_make_list,vehicle_model_list
from spares_tracker.api.mixins import ApiAuthMixin
from spares_tracker.common.utils import get_object
from spares_tracker.setup.models import Country
from spares_tracker.files.models import File
from spares_tracker.api.utils import inline_serializer


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
        exterior_color = serializers.ChoiceField(choices=Vehicle.Color.choices, required=True)
        fuel = serializers.ChoiceField(choices=Vehicle.Fuel.choices, required=True)
        transmission = serializers.ChoiceField(choices = Vehicle.Transmission.choices ,required=True)
        body_type = serializers.ChoiceField(choices = Vehicle.BodyType.choices ,required=True)
        drive_train = serializers.ChoiceField(choices = Vehicle.DriveTrain.choices ,required=True)
        steering = serializers.ChoiceField(choices = Vehicle.Steering.choices ,required=True)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if created_vehicle := vehicle_create(**serializer.validated_data):
            data = self.OutputSerializer(created_vehicle).data

        return Response(data, status=status.HTTP_201_CREATED)


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

        number_plate = serializers.CharField(required=False, max_length=20)
        country_of_registration = serializers.PrimaryKeyRelatedField(required=False, queryset=Country.objects.all())
        chasis_number = serializers.CharField(required=False, max_length=255)
        registration_year = serializers.IntegerField(required=False)
        registration_month = serializers.ChoiceField(choices=MONTH_CHOICES, required=False)
        manufacture_year = serializers.IntegerField(required=False)
        manufacture_month = serializers.ChoiceField(choices=MONTH_CHOICES, required=False)
        vehicle_model = serializers.PrimaryKeyRelatedField(queryset=VehicleModel.objects.all(), required=False)
        vehicle_model_code = serializers.CharField(required=False, max_length=255)
        engine_size = serializers.IntegerField(required=False)
        exterior_color = serializers.ChoiceField(choices=Vehicle.Color.choices, required=False)
        fuel = serializers.ChoiceField(choices=Vehicle.Fuel.choices, required=False)
        transmission = serializers.ChoiceField(choices = Vehicle.Transmission.choices ,required=False)
        body_type = serializers.ChoiceField(choices = Vehicle.BodyType.choices ,required=False)
        drive_train = serializers.ChoiceField(choices = Vehicle.DriveTrain.choices ,required=False)
        steering = serializers.ChoiceField(choices = Vehicle.Steering.choices ,required=False)
        vehicle_image = serializers.PrimaryKeyRelatedField(queryset=File.objects.all(), required=False)


    def post(self, request, vehicle_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        vehicle = get_object(Vehicle, pk=vehicle_id)

        vehicle_update(vehicle=vehicle, data=serializer.validated_data)

        return Response(status=status.HTTP_200_OK)


class VehicleListApi(ApiAuthMixin, APIView):
    class FileOutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        file_name = serializers.CharField()
        file_type = serializers.CharField()
        file = serializers.FileField()

    class OutputSerializer(serializers.Serializer):
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

        id = serializers.IntegerField()
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
        exterior_color = serializers.ChoiceField(choices=Vehicle.Color.choices, required=True)
        fuel = serializers.ChoiceField(choices=Vehicle.Fuel.choices, required=True)
        transmission = serializers.ChoiceField(choices = Vehicle.Transmission.choices ,required=True)
        body_type = serializers.ChoiceField(choices = Vehicle.BodyType.choices ,required=True)
        drive_train = serializers.ChoiceField(choices = Vehicle.DriveTrain.choices ,required=True)
        steering = serializers.ChoiceField(choices = Vehicle.Steering.choices ,required=True)
        removed = serializers.BooleanField(required=False)
        vehicle_image = inline_serializer(fields={
            'file': serializers.FileField()
        })

    class FilterSerializer(serializers.Serializer):
        number_plate = serializers.CharField(required=False, max_length=20)

    def get(self, request):
        # Make sure the filters are valid if passed
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        vehicles = vehicle_list(filters=filters_serializer.validated_data)

        data = self.OutputSerializer(vehicles, many=True).data
        return Response(data)


class VehicleDetailApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
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

        id = serializers.IntegerField()
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
        exterior_color = serializers.ChoiceField(choices=Vehicle.Color.choices, required=True)
        fuel = serializers.ChoiceField(choices=Vehicle.Fuel.choices, required=True)
        transmission = serializers.ChoiceField(choices = Vehicle.Transmission.choices ,required=True)
        body_type = serializers.ChoiceField(choices = Vehicle.BodyType.choices ,required=True)
        drive_train = serializers.ChoiceField(choices = Vehicle.DriveTrain.choices ,required=True)
        steering = serializers.ChoiceField(choices = Vehicle.Steering.choices ,required=True)
        removed = serializers.BooleanField(required=False)
        vehicle_image = inline_serializer(fields={
            'file': serializers.FileField()
        })

    def get(self, request, vehicle_id):
        vehicle = vehicle_detail(pk=vehicle_id)

        data = self.OutputSerializer(vehicle).data
        return Response(data)


class VehicleDeleteApi(ApiAuthMixin, APIView):
    def post(self, request, vehicle_id):
        vehicle = get_object(Vehicle, pk=vehicle_id)

        vehicle_delete(vehicle=vehicle)

        return Response(status=status.HTTP_200_OK)


class VehicleMakeApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        vehicle_make_name = serializers.CharField(required=True, max_length=255)
        image = inline_serializer(fields={
            'file': serializers.FileField()
        })

    def get(self, request):
        vehicle_makes = vehicle_make_list()

        data = self.OutputSerializer(vehicle_makes, many=True).data
        return Response(data)


class VehicleModelApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        vehicle_model_name = serializers.CharField(required=True, max_length=255)
        vehicle_make = serializers.PrimaryKeyRelatedField(queryset=VehicleMake.objects.all())

    class FilterSerializer(serializers.Serializer):
        vehicle_make = serializers.PrimaryKeyRelatedField(queryset=VehicleMake.objects.all())

    def get(self, request):
        # Make sure the filters are valid if passed
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        vehicle_models = vehicle_model_list(filters=filters_serializer.validated_data)

        data = self.OutputSerializer(vehicle_models, many=True).data
        return Response(data)
