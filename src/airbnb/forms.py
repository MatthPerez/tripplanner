from django import forms
from airbnb.models import Airbnb


class AddAirbnb(forms.ModelForm):
    class Meta:
        model = Airbnb
        fields = [
            "name",
            "countries",
            "reference",
            "price",
            "charges",
            "start_date",
            "end_date",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Joli studio bord de mer",
                    "autofocus": "autofocus",
                }
            ),
            "countries": forms.CheckboxSelectMultiple(),
            "reference": forms.TextInput(
                attrs={
                    "placeholder": "Référence unique",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "placeholder": "70",
                }
            ),
            "charges": forms.NumberInput(
                attrs={
                    "placeholder": "25",
                }
            ),
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
        labels = {
            "name": "Désignation",
            "countries": "Destinations",
            "reference": "Référence",
            "price": "Prix/nuit",
            "charges": "Frais",
            "start_date": "Date de début",
            "end_date": "Date de fin",
        }


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
