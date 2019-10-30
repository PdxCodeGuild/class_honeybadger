from django.urls import path
from . import views

app_name='contacts'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('detail/<int:item_id>/', views.detail, name="detail"),
    path('detail/<int:item_id>/edit/', views.edit, name="edit"),
]