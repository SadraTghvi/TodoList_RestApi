from api.views import *
from django.urls import path, include

urlpatterns = [
    path("", apiOverview, name="apiOverview"),
    path("task-list/", taskList, name="task-list"),
    path("task-detail/<str:pk>/", taskDetail, name="task-detail"),
]


app_name = "api"
