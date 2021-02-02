# coding: UTF-8
from django.urls import path

# Import du module views de l'application users
from runners import views

app_name = "runners"
urlpatterns = [
    path("test/", views.defaultView, name="default"),
    path("create/", views.create, name="create"),
]
