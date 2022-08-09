from django.urls import path

from .apis import (
    RepairListApi,
    RepairCreateApi,
    RepairProblemListApi
)

urlpatterns = [
    path('', RepairListApi.as_view(), name='repair_list'),
    path('problems/', RepairProblemListApi.as_view(), name='repair_problem_list'),
    path('create/', RepairCreateApi.as_view(), name='repair_create'),
]