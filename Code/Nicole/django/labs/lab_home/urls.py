# lab_home/urls.py

from django.urls import path
from . import views

app_name = "lab_home"
urlpatterns = [
    path("", views.index, name="index"),    
]