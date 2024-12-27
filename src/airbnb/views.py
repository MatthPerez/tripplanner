from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .forms import AddAirbnb
from .models import Airbnb
from django.utils.timezone import now
# from django.contrib.auth.mixins import UserPassesTestMixin


# def is_admin(user):
#     return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class AirbnbView(View):
    def get(self, request):
        today = now()
        airbnbs = Airbnb.objects.filter(start_date__gte=today,).order_by("city", "name")
        
        context = {
            "airbnbs": airbnbs,
        }
        
        return render(
            request,
            "airbnb/index.html",
            context,
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
    
    def post(self, request):
        form = AddAirbnb(request.POST)
        
        if form.is_valid():
            form.save()
            
            context={
                "form": form,
                "success": "Logement ajouté avec succès.",
            }
            
            return redirect("airbnb")
        else:
            print(form.errors)
            
            context={
                "form": form,
                "errors": form.errors,
            }
            
            return render(
                request,
                "airbnb/new.html",
                context
            )
            
            
        
class AirbnbUpdate(View):
    def get(self, request, pk):
        airbnb = Airbnb.objects.get(pk=pk)
        title=f"Mise à jour du logenemt : {airbnb.name}"
        submit_text="Enregistrer"
        
        # form = AddAirbnb(instance=airbnb)
        
        form = AddAirbnb(
            instance=airbnb,
            initial={
                "name": airbnb.name,
                "reference": airbnb.reference,
                "price": airbnb.price,
                "charges": airbnb.charges,
                "city": airbnb.city,
                "start_date": airbnb.start_date.strftime("%Y-%m-%d"),
                "end_date": airbnb.end_date.strftime("%Y-%m-%d"),
            }
        )
        
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
        
    def post(self, request, pk):
        airbnb = Airbnb.objects.get(pk=pk)
        form = AddAirbnb(request.POST, instance=airbnb)
        
        if form.is_valid():
            form.save()
            
            context={
                "form": form,
                "success": "Logement modifié avec succès.",
            }
            
            return redirect("airbnb")
        else:
            print(form.errors)
            
            context={
                "form": form,
                "errors": form.errors,
            }
            
            return render(
                request,
                "airbnb/new.html",
                context
            )
            
class AirbnbDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        airbnb = get_object_or_404(Airbnb, pk=pk)
        airbnb.delete()
        
        return redirect("airbnb")