from django import forms
from .models import Trip
from travel.models import Travel
from airbnb.models import Airbnb
from activity.models import Activity
from expense.models import Expense

class AddTrip(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['date', 'duration', 'place', 'people', 'travels', 'airbnbs', 'activities', 'expenses',]
    
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
    duration = forms.IntegerField(
        required=True,
        label="Durée (jours)",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "6",
            }
        ),
    )
    place = forms.CharField(
        required=True,
        label="Lieu",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Zadar, Croatie",
            }
        ),
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
    travels = forms.MultipleChoiceField(
        required=False,
        label="Trajets",
        choices=[(t.id, str(t)) for t in Travel.objects.all()],
        widget=forms.CheckboxSelectMultiple,
    )
    airbnbs = forms.MultipleChoiceField(
        required=False,
        label="Logements",
        choices=[(a.id, a.name) for a in Airbnb.objects.all()],
        widget=forms.CheckboxSelectMultiple,
    )
    activities = forms.MultipleChoiceField(
        required=False,
        label="Activités",
        choices=[(a.id, a.name) for a in Activity.objects.all()],
        widget=forms.CheckboxSelectMultiple,
    )
    expenses = forms.MultipleChoiceField(
        required=False,
        label="Dépenses",
        choices=[(e.id, e.name) for e in Expense.objects.all()],
        widget=forms.CheckboxSelectMultiple,
    )
    
class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
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
        self.fields['date'].widget.format = '%d/%m/%Y'