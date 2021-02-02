# from .forms import RunnersFormCreate
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import RunnersModel
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# View
def defaultView(request):
    return render(
        request,
        "runners/test.html",
        {
            "message": "Hello Runners!",
        },
    )


class RunnersCreate(CreateView):
    model = RunnersModel
    fields = ["websites", "checkers"]
    success_url = "/runners/test"

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse("websites:default"))

    def form_valid(self, form):
        # TODO execute COMMAND
        response = super().form_valid(form)
        return response


def listRunners(request):
    runners = RunnersModel.objects.order_by("-created")
    return render(
        request,
        "runners/list.html",
        {
            "runners": runners,
        },
    )