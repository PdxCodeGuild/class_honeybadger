
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'favnumapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('save_favnum/', views.save_favnum, name='save_favnum'),
    path('get_fav_nums/', views.get_fav_nums, name='get_fav_nums'),
    path('save_favnum_ajax/', views.save_favnum_ajax, name='save_favnum_ajax'),
]
