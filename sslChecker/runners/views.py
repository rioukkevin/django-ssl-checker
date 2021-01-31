from django.shortcuts import render
from django.http import HttpResponse

# View
def defaultView(request):
    return render(
        request,
        "runners/test.html",
        {
            "message": "Hello Runners!",
        },
    )