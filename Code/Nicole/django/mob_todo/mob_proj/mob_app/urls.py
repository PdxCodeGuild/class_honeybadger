from django.contrib import admin
from django.urls import path
from . import views

app_name = "mob_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("new_todo/", views.new_todo, name="new_todo"),
    path("details/<int:list_id>/", views.details, name="details"),
    path("completed/<int:item_id>/", views.completed, name="completed"),
    path("delete_completed/<int:list_id>/", views.delete_completed, name="delete_completed"),
]