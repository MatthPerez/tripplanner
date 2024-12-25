from django import forms
from .models import Expense

class AddExpense(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'place', 'category', 'price', 'note']
    
    name = forms.CharField(
        required=True,
        label="Désignation",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Location véhicule",
                "autofocus": "autofocus",
            }
        ),
    )
    place = forms.CharField(
        required=True,
        label="Ville",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Hertz, Zadar",
            }
        ),
    )
    category = forms.CharField(
        required=True,
        label="Catégorie",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Déplacement",
            }
        ),
    )
    price = forms.IntegerField(
        required=True,
        label="Prix",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "400",
            }
        ),
    )
    note = forms.CharField(
        required=False,
        label="Note, information",
        widget=forms.TextInput(
            attrs={
                "placeholder": "A réserver sur le site Internet",
            }
        ),
    )
    

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)