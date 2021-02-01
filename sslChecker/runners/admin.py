from django.contrib import admin

# Register your models here.
from checkers.models import CheckersModel
from runners.models import RunnersModel
from websites.models import WebsitesModel

admin.site.register(WebsitesModel)
admin.site.register(RunnersModel)
admin.site.register(CheckersModel)