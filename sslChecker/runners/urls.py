# coding: UTF-8
from .views import RunnersCreate
from django.urls import path

# Import du module views de l'application users
from runners import views

app_name = "runners"
urlpatterns = [
    path("test/", views.defaultView, name="default"),
    path("create/", RunnersCreate.as_view(), name="create"),
]
