from django.urls import path
from . import views

app_name = "lab_04_library"
urlpatterns = [
    path("", views.index, name = "index"),
]