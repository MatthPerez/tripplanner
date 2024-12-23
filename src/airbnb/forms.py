from django import forms
from airbnb.models import Airbnb

class AddAirbnb(forms.ModelForm):
    class Meta:
        model = Airbnb
        fields = ['name', 'reference', 'price', 'charges', 'city', 'start_date', 'end_date']
    
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
        widget=forms.NumberInput(
            attrs={
                "placeholder": "70",
            }
        ),
    )
    charges = forms.IntegerField(
        required=True,
        label="Frais",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "25",
            }
        ),
    )
    city = forms.CharField(
        required=True,
        max_length=50,
        label="Ville",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Barcelone",
            }
        ),
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