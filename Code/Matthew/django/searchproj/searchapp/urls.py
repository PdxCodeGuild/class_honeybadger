
from django.urls import path
from . import views

app_name = 'searchapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_search_terms/', views.get_search_terms, name='get_search_terms'),
]
