from django import forms

from .models import WebsitesModel

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class FormWithSubmit(forms.Form):
    helper = FormHelper()
    helper.add_input(
        Submit(
            "submit",
            "Créer un runner",
            css_class="btn btn-lg btn-primary btn-block bg_main",
        )
    )
    helper.form_method = "POST"


class RunnersFormCreate(FormWithSubmit):
    website = forms.ChoiceField(
        label="Nom du site web",
        choices=[],
        required=True,
    )

    def clean(self):
        cleaned_data = super(RunnersFormCreate, self).clean()
        # raise forms.ValidationError("Ce site web existe déjà")

        return cleaned_data
