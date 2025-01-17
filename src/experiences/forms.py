from django import forms
from .models import Experience
from country.models import Country


class AddExperience(forms.ModelForm):
    class Meta:
        model = Experience
        fields = [
            "name",
            "url",
            "note",
        ]

    name = forms.CharField(
        required=True,
        label="Désignation",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Restaurant thème japonais",
                "autofocus": "autofocus",
            }
        ),
    )
    url = forms.URLField(
        required=True,
        label="Lien",
        widget=forms.TextInput(
            attrs={
                "placeholder": "https://www.japonais.com",
            }
        ),
    )
    note = forms.CharField(
        required=False,
        label="Note, information",
        widget=forms.TextInput(
            attrs={
                "placeholder": "A faire en amoureux",
            }
        ),
    )


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
