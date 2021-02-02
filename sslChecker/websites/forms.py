from django import forms

from .models import WebsitesModel

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class FormWithSubmit(forms.Form):
    helper = FormHelper()
    helper.add_input(
        Submit(
            "submit", "Valider", css_class="btn btn-lg btn-primary btn-block bg_main"
        )
    )
    helper.form_method = "POST"


class WebsiteFormCreate(FormWithSubmit):
    website = forms.CharField(
        label="Nom du site web",
        max_length=128,
        required=True,
    )
    url = forms.URLField(
        label="Url du site web",
        required=True,
    )

    def clean(self):
        cleaned_data = super(WebsiteFormCreate, self).clean()
        try:
            WebsitesModel.objects.get(name=cleaned_data["website"])
        except WebsitesModel.DoesNotExist:
            pass
        else:
            raise forms.ValidationError("Ce site web existe déjà")

        return cleaned_data
