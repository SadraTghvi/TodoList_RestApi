from api.views import *
from django.urls import path, include

urlpatterns = [
    path("", apiOverview, name="apiOverview"),
    path("task-list/", taskList, name="task-list"),
    path("task-detail/<str:pk>/", taskDetail, name="task-detail"),
    path("task-create/", taskCreate, name="task-create"),
    path("task-update/", taskUpdate, name="task-update"),
    path("task-delete/", taskDelete, name="task-delete"),
]


app_name = "api"
