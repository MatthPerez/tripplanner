from django import forms
from .models import Country


class AddCountry(forms.ModelForm):
    class Meta:
        model = Country
        fields = ["name"]

    name = forms.CharField(
        required=True,
        label="Nom",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Bulgarie",
                "autofocus": "autofocus",
            }
        ),
    )


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
