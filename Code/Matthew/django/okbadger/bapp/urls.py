

from django.urls import path
from . import views

app_name = 'bapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:profile_id>/', views.profile, name='profile'),
    path('create/', views.create, name='create'),
    path('save_profile/', views.save_profile, name='save_profile')
]


