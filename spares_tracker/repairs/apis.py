from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from spares_tracker.api.mixins import ApiAuthMixin
from spares_tracker.repairs.selectors import repair_list
from spares_tracker.spareparts.models import SparePart
from spares_tracker.repairs.models import RepairProblem
from spares_tracker.repairs.services import repair_create
from spares_tracker.vehicles.models import Vehicle


# Repair endpoints
class RepairCreateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())
        problem_description = serializers.CharField()
        solution_description = serializers.CharField()
        spare_parts = serializers.CharField()
        problems = serializers.CharField()

    def post(self, request):

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        repair_create(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)

class RepairListApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        class VehicleSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            number_plate = serializers.CharField(max_length=20)
        class SparePartSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            name = serializers.CharField(max_length=255)
            code = serializers.CharField(max_length=255)
        class RepairProblemSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            name = serializers.CharField(max_length=255)
            description = serializers.CharField()

        id = serializers.IntegerField()
        vehicle = VehicleSerializer()
        problem_description = serializers.CharField()
        solution_description = serializers.CharField()
        spare_parts = SparePartSerializer(many=True)
        problems = RepairProblemSerializer(many=True)
        created_at = serializers.DateTimeField()

    class FilterSerializer(serializers.Serializer):
        vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all(), required=False)

    def get(self, request):
        # Make sure the filters are valid
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        repairs = repair_list(filters=filters_serializer.validated_data)

        data = self.OutputSerializer(repairs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
