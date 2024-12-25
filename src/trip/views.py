from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from .forms import AddTrip
from .models import Trip
from django.utils.timezone import now
# from django.contrib.auth.mixins import UserPassesTestMixin


# def is_admin(user):
#     return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class TripView(View):
    def get(self, request):
        today = now()
        trips = Trip.objects.filter(date__gte=today,).order_by("date")
        
        context = {
            "trips": trips,
        }
        
        return render(
            request,
            "trip/index.html",
            context,
        )
        
class TripDetail(DetailView):
    model = Trip
    template_name = "trip/detail.html"
    context_object_name = "trip"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['travels'] = context['trip'].travels.all()
        context['housing'] = context['trip'].housing.all()
        context['activities'] = context['trip'].activities.all()
        context['expenses'] = context['trip'].expenses.all()
        context['total_price'] = context['trip'].total_price
        
        return context
        
class NewTrip(View):
    def get(self, request):
        form = AddTrip()
        title="Ajouter un voyage"
        submit_text = "Ajouter"
        
        context = {
            "form": form,
            "title": title,
            "submit_text": submit_text,
        }
        
        return render(
            request,
            "trip/new.html",
            context,
        )
    
    def post(self, request):
        form = AddTrip(request.POST)
        
        if form.is_valid():
            form.save()
            
            context={
                "form": form,
                "success": "Trajet ajouté avec succès.",
            }
            
            return redirect("trip")
        else:
            print(form.errors)
            
            context={
                "form": form,
                "errors": form.errors,
            }
            
            return render(
                request,
                "trip/new.html",
                context
            )
            
            
        
class TripUpdate(View):
    def get(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        title=f"Mise à jour du trajet"
        submit_text="Enregistrer"
        
        form = AddTrip(
            initial={
                "date": trip.date.strftime("%Y-%m-%d"),
                "duration": trip.duration,
                "place": trip.place,
                "people": trip.people,
                "travels": trip.travels,
                "housing": trip.housing,
                "activities": trip.activities,
                "expenses": trip.expenses,
            }
        )
        
        context = {
            "form": form,
            "title": title,
            "submit_text": submit_text,
        }
        
        return render(
            request,
            "trip/new.html",
            context,
        )
        
    def post(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        
        form = AddTrip(request.POST, instance=trip)
        
        if form.is_valid():
            form.save()
            
            context={
                "form": form,
                "success": "Trajet modifié avec succès.",
            }
            
            return redirect("trip")
        else:
            print(form.errors)
            
            context={
                "form": form,
                "errors": form.errors,
            }
            
            return render(
                request,
                "trip/new.html",
                context
            )
            
class TripDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        trip = get_object_or_404(Trip, pk=pk)
        trip.delete()
        
        return redirect("trip")