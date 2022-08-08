from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from spares_tracker.api.mixins import ApiAuthMixin
from spares_tracker.common.utils import inline_serializer
from spares_tracker.spareparts.models import SparePart, SparePartCategory, SparePartPurchase
from spares_tracker.spareparts.selectors import sparepart_category_list, sparepart_list, sparepart_purchase_detail, sparepart_purchase_list
from spares_tracker.employee.models import Employee
from spares_tracker.spares_tracker.spareparts.services import sparepart_purchase_create
from spares_tracker.suppliers.models import Supplier
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


# spare part purchase endpoints
class SparePartPurchaseCreateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        spare_part = serializers.PrimaryKeyRelatedField(queryset=SparePart.objects.all(), required=True)
        order_number = serializers.CharField(max_length=255, required=False)
        quantity = serializers.IntegerField(required=True)
        unit_price = serializers.DecimalField(max_digits=15, decimal_places=2, required=True)
        amount_paid = serializers.DecimalField(max_digits=15, decimal_places=2, required=True)
        supplied_by = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(), required=True)
        received_by = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), required=True)

    class FilterSerializer(serializers.Serializer):
        spare_part = serializers.PrimaryKeyRelatedField(queryset=SparePart.objects.all(), required=False)
        order_number = serializers.CharField(required=False)

    def get(self, request):
        # Make sure the filters are valid
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        sparepart_purchases = sparepart_purchase_create(filters=filters_serializer.validated_data)

        data = self.InputSerializer(sparepart_purchases, many=True).data
        return Response(data, status=status.HTTP_200_OK)

class SparePartPurchaseListApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        spare_part = serializers.PrimaryKeyRelatedField(queryset=SparePart.objects.all(), required=True)
        order_number = serializers.CharField(max_length=255, required=False)
        quantity = serializers.IntegerField(required=True)
        unit_price = serializers.DecimalField(max_digits=15, decimal_places=2, required=True)
        amount_paid = serializers.DecimalField(max_digits=15, decimal_places=2, required=True)
        supplied_by = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(), required=True)
        received_by = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), required=True)

    class FilterSerializer(serializers.Serializer):
        spare_part = serializers.PrimaryKeyRelatedField(queryset=SparePart.objects.all(), required=False)
        order_number = serializers.CharField(required=False)

    def get(self, request):
        # Make sure the filters are valid
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        sparepart_purchases = sparepart_purchase_list(filters=filters_serializer.validated_data)

        data = self.OutputSerializer(sparepart_purchases, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class SparePartPurchaseDetailApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        spare_part = serializers.PrimaryKeyRelatedField(queryset=SparePart.objects.all(), required=True)
        order_number = serializers.CharField(max_length=255, required=False)
        quantity = serializers.IntegerField(required=True)
        unit_price = serializers.DecimalField(max_digits=15, decimal_places=2, required=True)
        amount_paid = serializers.DecimalField(max_digits=15, decimal_places=2, required=True)
        supplied_by = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(), required=True)
        received_by = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), required=True)


    def get(self, request, sparepart_purchase_id):
        sparepart_purchase = sparepart_purchase_detail(pk=sparepart_purchase_id)

        data = self.OutputSerializer(sparepart_purchase).data
        return Response(data)
