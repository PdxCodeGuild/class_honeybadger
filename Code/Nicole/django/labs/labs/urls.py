from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("lab_01_polls/", include("lab_01_polls.urls")),
    path('admin/', admin.site.urls),
]
