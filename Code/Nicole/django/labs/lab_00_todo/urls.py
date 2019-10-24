# lab_01_polls/urls.py

from django.urls import path
from . import views

app_name = "lab_00_todo"

urlpatterns = [
    path("", views.index, name="index"),    
]