from django.contrib import admin
from . import views
from django.urls import path

app_name = "todoapp"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('new_todo/', views.new_todo, name='new_todo'),
    path('details/<int:list_id>/', views.details, name='details'),
    path('completed/<int:item_id>/', views.completed, name='completed'),
    path('delete_completed/<int:list_id>/', views.delete_completed, name='delete_completed'),

]
