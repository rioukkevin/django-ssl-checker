# coding: UTF-8
from django.urls import path

# Import du module views de l'application users
from websites import views

app_name = "websites"
urlpatterns = [
    path("test/", views.defaultView, name="default"),
    path("create/", views.create, name="create"),
]