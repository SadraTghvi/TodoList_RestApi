from api.views import *
from django.urls import path, include

urlpatterns = [
    path("",home,name="home")
]


app_name = "api"
