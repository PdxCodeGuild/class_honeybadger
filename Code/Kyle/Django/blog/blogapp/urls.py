from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_post_id>/', views.about, name='about')
]
