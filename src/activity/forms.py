from django import forms
from .models import Activity

class AddActivity(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'city', 'price_person', 'category', 'gps', 'note']
    
    name = forms.CharField(
        required=True,
        label="Désignation",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Restaurant étoilé",
                "autofocus": "autofocus",
            }
        ),
    )
    city = forms.CharField(
        required=True,
        label="Ville",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Centre-ville de Zadar",
            }
        ),
    )
    price_person = forms.IntegerField(
        required=True,
        label="Prix par personne",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "40",
            }
        ),
    )
    category = forms.CharField(
        required=True,
        label="Lieu de départ",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Restauration",
            }
        ),
    )
    gps = forms.CharField(
        required=False,
        label="Lieu de départ",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'xxxx yyyy',
            }
        ),
    )
    note = forms.CharField(
        required=True,
        label="Note, information",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ouvert de 6h à 23h",
            }
        ),
    )
    

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)