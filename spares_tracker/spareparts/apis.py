from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from spares_tracker.api.mixins import ApiAuthMixin
from spares_tracker.common.utils import inline_serializer
from spares_tracker.spareparts.models import SparePartCategory
from spares_tracker.spareparts.selectors import sparepart_category_list, sparepart_list
from spares_tracker.vehicles.models import VehicleModel




class SparePartCategoryListApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        category_name = serializers.CharField(max_length=255)
        image = inline_serializer(fields={
            'file': serializers.FileField()
        })
        relates_to = serializers.PrimaryKeyRelatedField(queryset=SparePartCategory.objects.all())

    class FilterSerializer(serializers.Serializer):
        category_name = serializers.CharField(max_length=255, required=False)
        relates_to = serializers.PrimaryKeyRelatedField(queryset=SparePartCategory.objects.all(), required=False)

    def get(self, request):
        # Make sure the filters are valid
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        sparepart_categories = sparepart_category_list(filters=filters_serializer.validated_data)

        data = self.OutputSerializer(sparepart_categories, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class SparePartListApi(ApiAuthMixin, APIView):

    class OutputSerializer(serializers.Serializer):
        class VehicleModelSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            vehicle_model_name = serializers.CharField(required=True, max_length=255)

        id = serializers.IntegerField()
        name = serializers.CharField(max_length=255)
        code = serializers.CharField(max_length=255)
        quantity = serializers.IntegerField()
        price = serializers.DecimalField(max_digits=15, decimal_places=2)
        image = inline_serializer(fields={
            'file': serializers.FileField()
        })
        category = serializers.PrimaryKeyRelatedField(queryset=SparePartCategory.objects.all())
        # vehicle_models = serializers.PrimaryKeyRelatedField(queryset=VehicleModel.objects.all(), many=True)
        vehicle_models = VehicleModelSerializer(many=True)
    class FilterSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255, required=False)
        code = serializers.CharField(max_length=255, required=False)
        category = serializers.PrimaryKeyRelatedField(queryset=SparePartCategory.objects.all(), required=False)
        vehicle_models = serializers.PrimaryKeyRelatedField(queryset=VehicleModel.objects.all(), many=True)


    def get(self, request):
        # Make sure the filters are valid
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        spareparts = sparepart_list(filters=filters_serializer.validated_data)

        data = self.OutputSerializer(spareparts, many=True).data
        return Response(data, status=status.HTTP_200_OK)
