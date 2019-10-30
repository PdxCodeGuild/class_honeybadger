from django.urls import path
from . import views

app_name = "lab_02_contacts"
urlpatterns = [
    path("", views.index, name = "index"),
    path("add_contact/", views.add_contact, name="add_contact"),
]