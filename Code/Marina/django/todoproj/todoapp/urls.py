from . import views
from django.urls import path

app_name = "todoapp"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create_todopost/', views.create_todopost, name='create_todopost'),
    path('<str:todo_post_slug>/', views.detail, name='detail')
]
