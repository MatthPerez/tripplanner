from django import forms
from .models import Activity
from country.models import Country


class AddActivity(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ["name", "countries", "price_person", "category", "gps", "note"]

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
    countries = forms.ModelMultipleChoiceField(
        queryset=Country.objects.all().order_by(
            "name"
        ),
        label="Destinations",
        widget=forms.CheckboxSelectMultiple,
    )
    price_person = forms.DecimalField(
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
        label="Catégorie",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Restauration",
            }
        ),
    )
    gps = forms.CharField(
        required=False,
        label="Point GPS",
        widget=forms.TextInput(
            attrs={
                "placeholder": "xxxx yyyy",
            }
        ),
    )
    note = forms.CharField(
        required=False,
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
