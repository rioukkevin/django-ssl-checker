# coding: UTF-8
from django.urls import path

# Import du module views de l'application users
from checkers import views

app_name = "checkers"
urlpatterns = [
    path("test/", views.defaultView, name="default"),
]
