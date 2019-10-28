
from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:blog_post_id>/', views.detail, name='detail'),
    path('create/', views.create_blogpost, name='create_blogpost')
]