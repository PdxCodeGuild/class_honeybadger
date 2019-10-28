# lab_01_polls/urls.py

from django.urls import path
from . import views

app_name = "lab_00_todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("complete_todo/", views.complete_todo, name="complete_todo"),
    path("add_todo/", views.add_todo, name="add_todo"),
    path("delete_todo/", views.delete_todo, name="delete_todo"),
    path("undo_todo/", views.undo_todo, name="undo_todo"),
]