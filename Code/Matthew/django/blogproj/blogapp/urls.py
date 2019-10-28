
from django.urls import path

from . import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_blogpost/', views.create_blogpost, name='create_blogpost'),
    path('<str:blog_post_slug>/', views.detail, name='detail'),
]
