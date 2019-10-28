from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_todo/', views.new_todo, name='new_todo'),
    path('complete_todo/', views.complete_todo, name='complete_todo')
]