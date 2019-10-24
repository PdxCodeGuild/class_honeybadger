
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:blog_post_id>/', views.detail),
]
