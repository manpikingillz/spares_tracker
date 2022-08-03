from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from spares_tracker.api.mixins import ApiAuthMixin
from spares_tracker.suppliers.services import supplier_create


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