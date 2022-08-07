from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from spares_tracker.api.mixins import ApiAuthMixin
from spares_tracker.common.utils import inline_serializer
from spares_tracker.spareparts.models import SparePartCategory
from spares_tracker.spareparts.selectors import sparepart_category_list




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
