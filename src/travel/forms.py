from django import forms
from .models import Travel

class AddTravel(forms.ModelForm):
    class Meta:
        model = Travel
        fields = ['date', 'price', 'start_place', 'start_time', 'end_place', 'end_time', 'type']
    
    date = forms.DateField(
        required=True,
        label="Date",
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "placeholder": "AAAA-MM-JJ",
                "autofocus": "autofocus",
            }
        ),
    )
    price = forms.CharField(
        required=True,
        label="Prix",
        widget=forms.TextInput(
            attrs={
                "placeholder": "90",
            }
        ),
    )
    start_place = forms.CharField(
        required=True,
        label="Lieu de départ",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Gare TGV d'Avignon",
            }
        ),
    )
    start_time = forms.CharField(
        required=True,
        label="Heure de départ",
        widget=forms.TextInput(
            attrs={
                "placeholder": "5h45",
            }
        ),
    )
    end_place = forms.CharField(
        required=True,
        label="Lieu d'arrivée",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Gare TGV de Zadar",
            }
        ),
    )
    end_time = forms.CharField(
        required=True,
        label="Heure d'arrivée",
        widget=forms.TextInput(
            attrs={
                "placeholder": "12h20",
            }
        ),
    )
    type = forms.CharField(
        required=True,
        max_length=50,
        label="Type",
        widget=forms.TextInput(
            attrs={
                "placeholder": "TER, TGV, avion, etc.",
            }
        ),
    )
    

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "AAAA-MM-JJ"
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)