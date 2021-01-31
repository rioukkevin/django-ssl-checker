from django.shortcuts import render
from django.http import HttpResponse

# View
def defaultView(request):
    return HttpResponse("Hello Runners!")