from django.shortcuts import render
from django.views import View
from .forms import AirbnbForm, AddAirbnb
# from django.contrib.auth.mixins import UserPassesTestMixin


# def is_admin(user):
#     return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class Airbnb(View):
    def get(self, request):
        return render(
            request,
            "airbnb/index.html",
        )
        
class NewAirbnb(View):
    def get(self, request):
        form = AddAirbnb()
        title="Ajouter un logement"
        submit_text = "Ajouter"
        
        context = {
            "form": form,
            "title": title,
            "submit_text": submit_text,
        }
        
        return render(
            request,
            "airbnb/new.html",
            context,
        )