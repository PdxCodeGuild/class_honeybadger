from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    # path('create_todo', views.createtodo, name='createtodo')
]
