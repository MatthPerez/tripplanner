from django import forms
from airbnb.models import Airbnb

class AddAirbnb(forms.Form):
    name = forms.CharField(
        required=True,
        label="Désignation",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Joli studio bord de mer",
                "autofocus": "autofocus",
            }
        ),
    )
    reference = forms.CharField(
        required=True,
        label="Référence",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Référence unique",
            }
        ),
    )
    price = forms.IntegerField(
        required=True,
        label="Prix/nuit",
    )
    charges = forms.IntegerField(
        required=True,
        label="Frais",
    )
    city = forms.CharField(
        required=True,
        max_length=50,
        label="Ville",
    )
    start_date = forms.DateField(
        required=True,
        label="Date de début",
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "placeholder": "AAAA-MM-JJ",
            }
        ),
    )
    end_date = forms.DateField(
        required=True,
        label="Date de fin",
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "placeholder": "AAAA-MM-JJ",
            }
        ),
    )

class AirbnbForm(forms.ModelForm):
    class Meta:
        model = Airbnb
        fields = "__all__"
        widgets = {
            "start_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "AAAA-MM-JJ",
                }
            ),
            "end_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "AAAA-MM-JJ",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)