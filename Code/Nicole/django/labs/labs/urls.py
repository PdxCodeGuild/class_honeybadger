from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("lab_home.urls")),
    path("lab_01_polls/", include("lab_01_polls.urls")),
    path('admin/', admin.site.urls),
]
