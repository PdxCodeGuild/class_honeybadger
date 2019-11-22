
from django.urls import path
from . import views

app_name = 'urlapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('save_url/', views.save_url, name='save_url'),
    path('<str:code>/', views.redirect_url, name='redirect_url'),
]





