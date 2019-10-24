from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('<path>/', views.todo, name='todo')
]