"""sslChecker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
import runners
import websites
import checkers

urlpatterns = [
    path(r"", RedirectView.as_view(url="/runners/list")),
    path("admin/", admin.site.urls),
    path(r"checkers/", include("checkers.urls", namespace="checkers")),
    path(r"runners/", include("runners.urls", namespace="runners")),
    path(r"websites/", include("websites.urls", namespace="websites")),
]
