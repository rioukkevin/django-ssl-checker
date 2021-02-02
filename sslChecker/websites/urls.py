# coding: UTF-8
from .views import WebsitesCreate
from django.urls import path

# Import du module views de l'application users
from websites import views

app_name = "websites"
urlpatterns = [
    path("test/", views.defaultView, name="default"),
    path("list/", views.listWebsites, name="list"),
    path("create/", WebsitesCreate.as_view(), name="create"),
]