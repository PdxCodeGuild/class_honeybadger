
from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('favorites/', views.favorites, name='favorites'),
    path('favorite_blog_post/<int:blog_post_id>/', views.favorite_blog_post, name='favorite_blog_post')
]
