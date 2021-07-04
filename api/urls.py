from api.views import *
from django.urls import path, include

urlpatterns = [
    path("", apiOverview, name="apiOverview")
]


app_name = "api"
