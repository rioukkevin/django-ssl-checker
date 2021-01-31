from django.shortcuts import render
from django.http import HttpResponse

# View
def defaultView(request):
    return render(
        request,
        "websites/test.html",
        {
            "message": "Hello Websites!",
        },
    )