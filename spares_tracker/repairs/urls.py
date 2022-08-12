from django.urls import path

from .apis import (
    RepairListApi,
    RepairCreateApi,
    RepairProblemListApi,
    RepairDetailApi,
    RepairProblemRecommendationListApi
)

urlpatterns = [
    path('', RepairListApi.as_view(), name='repair_list'),
    path('problems/', RepairProblemRecommendationListApi.as_view(), name='repair_problem_recommendations_list'),
    path('<int:repair_id>/', RepairDetailApi.as_view(), name='repair_detail'),
    path('problems/', RepairProblemListApi.as_view(), name='repair_problem_list'),
    path('create/', RepairCreateApi.as_view(), name='repair_create'),
]