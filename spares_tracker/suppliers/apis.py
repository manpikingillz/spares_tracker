from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from spares_tracker.api.mixins import ApiAuthMixin
from spares_tracker.suppliers.services import supplier_create
from spares_tracker.suppliers.selectors import supplier_list


class SupplierCreateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255, required=True)
        email = serializers.EmailField(max_length=255, required=True)
        phone = serializers.CharField(max_length=30, required=True)
        address = serializers.CharField(max_length=255, required=True)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        supplier_create(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class SupplierListApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField(max_length=255, required=True)
        email = serializers.EmailField(max_length=255, required=True)
        phone = serializers.CharField(max_length=30, required=True)
        address = serializers.CharField(max_length=255, required=True)

    class FilterSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255, required=False)
        email = serializers.EmailField(max_length=255, required=False)
        phone = serializers.CharField(max_length=30, required=False)

    def get(self, request):
        # Make sure the filters are valid
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        suppliers = supplier_list(filters=filters_serializer.validated_data)

        data = self.OutputSerializer(suppliers, many=True).data
        return Response(data)