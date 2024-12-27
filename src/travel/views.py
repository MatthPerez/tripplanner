from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .forms import AddTravel
from .models import Travel
from django.utils.timezone import now
# from django.contrib.auth.mixins import UserPassesTestMixin


# def is_admin(user):
#     return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class TravelView(View):
    def get(self, request):
        today = now()
        travels = Travel.objects.filter(date__gte=today,).order_by("date")
        
        context = {
            "travels": travels,
        }
        
        return render(
            request,
            "travel/index.html",
            context,
        )

class NewTravel(View):
    def get(self, request):
        form = AddTravel()
        title="Ajouter un trajet"
        submit_text = "Ajouter"
        
        context = {
            "form": form,
            "title": title,
            "submit_text": submit_text,
        }
        
        return render(
            request,
            "travel/new.html",
            context,
        )
    
    def post(self, request):
        form = AddTravel(request.POST)
        
        if form.is_valid():
            form.save()
            
            context={
                "form": form,
                "success": "Trajet ajouté avec succès.",
            }
            
            return redirect("travel")
        else:
            print(form.errors)
            
            context={
                "form": form,
                "errors": form.errors,
            }
            
            return render(
                request,
                "travel/new.html",
                context
            )

class TravelUpdate(View):
    def get(self, request, pk):
        travel = Travel.objects.get(pk=pk)
        title=f"Mise à jour du trajet"
        submit_text="Enregistrer"

        form = AddTravel(
            instance=travel,
            initial={
                "date": travel.date.strftime("%Y-%m-%d"),
                "price": travel.price,
                "start_place": travel.start_place,
                "start_time": travel.start_time,
                "end_place": travel.end_place,
                "end_time": travel.end_time,
                "type": travel.type,
            }
        )

        context = {
            "form": form,
            "title": title,
            "submit_text": submit_text,
        }

        return render(
            request,
            "travel/new.html",
            context,
        )

    def post(self, request, pk):
        travel = Travel.objects.get(pk=pk)
        form = AddTravel(request.POST, instance=travel)

        if form.is_valid():
            form.save()

            context={
                "form": form,
                "success": "Trajet modifié avec succès.",
            }

            return redirect("travel")
        else:
            print(form.errors)

            context={
                "form": form,
                "errors": form.errors,
            }

            return render(
                request,
                "travel/new.html",
                context
            )

class TravelDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        travel = get_object_or_404(Travel, pk=pk)
        travel.delete()
        
        return redirect("travel")
