from django import forms
from .models import Trip
from travel.models import Travel
from country.models import Country
from airbnb.models import Airbnb
from activity.models import Activity
from expense.models import Expense


class AddTrip(forms.ModelForm):
    class Meta:
        model = Trip
        fields = [
            "date",
            "duration",
            "place",
            "people",
            "travels",
            "airbnbs",
            "activities",
            "expenses",
        ]

    place = forms.ModelChoiceField(
        required=True,
        queryset=Country.objects.all(),
        label="Destination",
        to_field_name="name",
        widget=forms.Select(attrs={"autofocus": True}),
    )
    date = forms.DateField(
        required=True,
        label="Date",
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "placeholder": "AAAA-MM-JJ",
            }
        ),
    )
    duration = forms.IntegerField(
        required=True,
        label="Durée (jours)",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "6",
            }
        ),
        min_value=1,
    )
    people = forms.IntegerField(
        required=True,
        label="Nombre de participants",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "2",
            }
        ),
    )
    travels = forms.ModelMultipleChoiceField(
        required=False,
        label="Trajets",
        queryset=Travel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    airbnbs = forms.ModelMultipleChoiceField(
        required=False,
        label="Logements",
        queryset=Airbnb.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    activities = forms.ModelMultipleChoiceField(
        required=False,
        label="Activités",
        queryset=Activity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    expenses = forms.ModelMultipleChoiceField(
        required=False,
        label="Dépenses",
        queryset=Expense.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
