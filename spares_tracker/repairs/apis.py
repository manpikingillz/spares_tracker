from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from spares_tracker.api.mixins import ApiAuthMixin
from spares_tracker.repairs.selectors import repair_comment_list, repair_detail, repair_list, repair_problem_list, repair_problem_recommendation_list, repair_sparepart_recommendation_list
from spares_tracker.spareparts.models import SparePart
from spares_tracker.repairs.models import Repair, RepairProblem, RepairProblemRecommendation, RepairSparePartRecommendation
from spares_tracker.repairs.services import repair_comment_create, repair_create, repair_problem_recommendation_update, repair_sparepart_recommendation_update, repair_update
from spares_tracker.common.utils import get_object
from spares_tracker.employee.models import Section
from spares_tracker.users.models import BaseUser
from spares_tracker.vehicles.models import Vehicle


# Repair endpoints
class RepairCreateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())
        problem_description = serializers.CharField()
        solution_description = serializers.CharField()
        spare_parts = serializers.CharField(required=False)
        problems = serializers.CharField(required=False)

    def post(self, request):
        user = get_object(BaseUser, pk=request.user.id)

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        repair_create(**serializer.validated_data, user=user)

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
        class SectionSerializer(serializers.Serializer):
            name = serializers.CharField()

        id = serializers.IntegerField()
        vehicle = VehicleSerializer()
        problem_description = serializers.CharField()
        solution_description = serializers.CharField()
        spare_parts = SparePartSerializer(many=True)
        problems = RepairProblemSerializer(many=True)
        created_at = serializers.DateTimeField()
        status = serializers.CharField(max_length=255)
        section = SectionSerializer()

    class FilterSerializer(serializers.Serializer):
        vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all(), required=False)

    def get(self, request):
        # Make sure the filters are valid
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        repairs = repair_list(filters=filters_serializer.validated_data)

        data = self.OutputSerializer(repairs, many=True).data
        return Response(data, status=status.HTTP_200_OK)

class RepairDetailApi(ApiAuthMixin, APIView):
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
        class SectionSerializer(serializers.Serializer):
            name = serializers.CharField()

        id = serializers.IntegerField()
        vehicle = VehicleSerializer()
        problem_description = serializers.CharField()
        solution_description = serializers.CharField()
        spare_parts = SparePartSerializer(many=True)
        problems = RepairProblemSerializer(many=True)
        created_at = serializers.DateTimeField()
        status = serializers.CharField(max_length=255)
        section = SectionSerializer()


    def get(self, request, repair_id):

        repair = repair_detail(pk=repair_id)

        data = self.OutputSerializer(repair,).data
        return Response(data, status=status.HTTP_200_OK)

class RepairUpdateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        status = serializers.ChoiceField(choices=Repair.Status.choices, required=False)
        section = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all(), required=False)

    def post(self, request, repair_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        repair = get_object(Repair, pk=repair_id)
        repair_update(repair=repair, data=serializer.validated_data)
        return Response(status=status.HTTP_200_OK)


class RepairProblemListApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):

        id = serializers.IntegerField()
        name = serializers.CharField()

    class FilterSerializer(serializers.Serializer):
        name = serializers.CharField(required=False)

    def get(self, request):
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        repairs = repair_problem_list(filters=filters_serializer.validated_data)

        data = self.OutputSerializer(repairs, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class RepairProblemRecommendationListApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        class RepairProblemSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            name = serializers.CharField(max_length=255)
        class BaseUserSerializer(serializers.Serializer):
            class EmployeeSerializer(serializers.Serializer):
                id = serializers.IntegerField()
                full_name = serializers.CharField(max_length=255, required=False)
                first_name = serializers.CharField(max_length=255, required=False)
                last_name = serializers.CharField(max_length=255, required=False)

            email = serializers.EmailField(max_length=255)
            employee = EmployeeSerializer()

        id = serializers.IntegerField()
        repair = serializers.PrimaryKeyRelatedField(queryset=Repair.objects.all(), required=False)
        problem = RepairProblemSerializer()
        added_by = BaseUserSerializer()

    class FilterSerializer(serializers.Serializer):
        repair = serializers.PrimaryKeyRelatedField(queryset=Repair.objects.all(), required=False)
        problem = serializers.PrimaryKeyRelatedField(queryset=RepairProblem.objects.all(), required=False)
        added_by = serializers.PrimaryKeyRelatedField(queryset=BaseUser.objects.all(), required=False)

    def get(self, request):
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        problems = repair_problem_recommendation_list(filters=filters_serializer.validated_data)

        data = self.OutputSerializer(problems, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class RepairSparePartRecommendationListApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        class SpartPartSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            name = serializers.CharField(max_length=255)
            quantity = serializers.IntegerField()
        class BaseUserSerializer(serializers.Serializer):
            class EmployeeSerializer(serializers.Serializer):
                id = serializers.IntegerField()
                full_name = serializers.CharField(max_length=255, required=False)
                first_name = serializers.CharField(max_length=255, required=False)
                last_name = serializers.CharField(max_length=255, required=False)

            email = serializers.EmailField(max_length=255)
            employee = EmployeeSerializer()

        id = serializers.IntegerField()
        repair = serializers.PrimaryKeyRelatedField(queryset=Repair.objects.all(), required=False)
        sparepart = SpartPartSerializer()
        added_by = BaseUserSerializer()

    class FilterSerializer(serializers.Serializer):
        repair = serializers.PrimaryKeyRelatedField(queryset=Repair.objects.all(), required=False)
        sparepart = serializers.PrimaryKeyRelatedField(queryset=SparePart.objects.all(), required=False)
        added_by = serializers.PrimaryKeyRelatedField(queryset=BaseUser.objects.all(), required=False)

    def get(self, request):
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        spareparts = repair_sparepart_recommendation_list(filters=filters_serializer.validated_data)

        data = self.OutputSerializer(spareparts, many=True).data
        return Response(data, status=status.HTTP_200_OK)

class RepairSparePartRecommendationUpdateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        repair = serializers.PrimaryKeyRelatedField(queryset=Repair.objects.all(), required=True)
        spareparts = serializers.CharField()

    def post(self, request):
        if not request.data.get('spareparts'):
            repair_id = request.data.get('repair', None)
            if repair_id is not None:
                #TODO: Refactor to put it in service
                RepairSparePartRecommendation.objects.filter(repair_id=int(repair_id)).delete()
        else:
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            repair_sparepart_recommendation_update(**serializer.validated_data, added_by=request.user)

        return Response(status=status.HTTP_200_OK)

class RepairProblemRecommendationUpdateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        repair = serializers.PrimaryKeyRelatedField(queryset=Repair.objects.all(), required=True)
        problems = serializers.CharField()

    def post(self, request):
        if not request.data.get('problems'):
            repair_id = request.data.get('repair', None)
            if repair_id is not None:
                #TODO: Refactor to put it in service
                RepairProblemRecommendation.objects.filter(repair_id=int(repair_id)).delete()
        else:
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            repair_problem_recommendation_update(**serializer.validated_data, added_by=request.user)

        return Response(status=status.HTTP_200_OK)

class RepairCommentCreateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        repair = serializers.PrimaryKeyRelatedField(queryset=Repair.objects.all())
        comment = serializers.CharField()
        commented_by = serializers.PrimaryKeyRelatedField(queryset=BaseUser.objects.all())

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        repair_comment_create(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)

class RepairCommentListApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        class BaseUserSerializer(serializers.Serializer):
            class EmployeeSerializer(serializers.Serializer):
                id = serializers.IntegerField()
                full_name = serializers.CharField(max_length=255, required=False)
                first_name = serializers.CharField(max_length=255, required=False)
                last_name = serializers.CharField(max_length=255, required=False)

            employee = EmployeeSerializer()
        id = serializers.IntegerField()
        repair = serializers.PrimaryKeyRelatedField(queryset=Repair.objects.all())
        comment = serializers.CharField()
        commented_by = BaseUserSerializer()
    class FilterSerializer(serializers.Serializer):
        repair = serializers.PrimaryKeyRelatedField(queryset=Repair.objects.all())

    def get(self, request):
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        repair_comments = repair_comment_list(filters=filters_serializer.validated_data)

        data = self.OutputSerializer(repair_comments, many=True).data
        return Response(data, status=status.HTTP_200_OK)
