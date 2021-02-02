from .forms import RunnersFormCreate
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# View
def defaultView(request):
    return render(
        request,
        "runners/test.html",
        {
            "message": "Hello Runners!",
        },
    )


def create(request):
    if request.method == "POST":
        form = RunnersFormCreate(request.POST)
        if form.is_valid():
            print("GOOD")
            return HttpResponseRedirect(reverse("websites:default"))
    else:
        form = RunnersFormCreate()
        print("NOT GOOD")
    return render(
        request,
        "create.html",
        {
            "url_form": reverse("runners:create"),
            "title": "Création d'un runner pour un site web",
            "form": form,
        },
    )