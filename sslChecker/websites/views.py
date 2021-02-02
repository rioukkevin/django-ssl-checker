from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import WebsiteFormCreate
from .models import WebsitesModel
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# View
def defaultView(request):
    return render(
        request,
        "websites/test.html",
        {
            "message": "Hello Websites!",
        },
    )


# def create(request):
#     if request.method == "POST":
#         form = WebsiteFormCreate(request.POST)
#         if form.is_valid():
#             website = form.cleaned_data["website"]
#             url = form.cleaned_data["url"]
#             website = WebsitesModel(
#                 name=website,
#                 url=url,
#             )
#             website.save()
#             return HttpResponseRedirect(reverse("websites:default"))
#     else:
#         form = WebsiteFormCreate()
#     return render(
#         request,
#         "create.html",
#         {
#             "url_form": reverse("websites:create"),
#             "title": "Création d'un site web",
#             "form": form,
#         },
#     )


class WebsitesCreate(CreateView):
    model = WebsitesModel
    fields = ["name", "url"]
    success_url = "/websites/list"

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse("websites:create"))

    def form_valid(self, form):
        # TODO execute COMMAND
        response = super().form_valid(form)
        return response


def listWebsites(request):
    websites = WebsitesModel.objects.order_by("name")
    return render(
        request,
        "websites/list.html",
        {
            "websites": websites,
        },
    )