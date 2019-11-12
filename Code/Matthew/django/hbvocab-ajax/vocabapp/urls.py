
from django.urls import path
from . import views

app_name = 'vocabapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_data/', views.get_data, name='get_data'),
    path('save_item/', views.save_item, name='save_item')
]