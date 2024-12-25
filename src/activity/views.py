from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .forms import AddActivity
from .models import Activity
# from django.contrib.auth.mixins import UserPassesTestMixin


# def is_admin(user):
#     return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class ActivityView(View):
    def get(self, request):
        activities = Activity.objects.order_by("name")
        
        context = {
            "activities": activities,
        }
        
        return render(
            request,
            "activity/index.html",
            context,
        )
        
class NewActivity(View):
    def get(self, request):
        form = AddActivity()
        title="Ajouter une activité"
        submit_text = "Ajouter"
        
        context = {
            "form": form,
            "title": title,
            "submit_text": submit_text,
        }
        
        return render(
            request,
            "activity/new.html",
            context,
        )
    
    def post(self, request):
        form = AddActivity(request.POST)
        
        if form.is_valid():
            form.save()
            
            context={
                "form": form,
                "success": "Activité ajoutée avec succès.",
            }
            
            return redirect("activity")
        else:
            print(form.errors)
            
            context={
                "form": form,
                "errors": form.errors,
            }
            
            return render(
                request,
                "activity/new.html",
                context
            )
            
            
        
class ActivityUpdate(View):
    def get(self, request, pk):
        activity = Activity.objects.get(pk=pk)
        title=f"Mise à jour de l'activité"
        submit_text="Enregistrer"
        
        form = AddActivity(
            initial={
                "name": activity.name,
                "city": activity.city,
                "price_person": activity.price_person,
                "category": activity.category,
                "gps": activity.gps,
                "note": activity.note,
            }
        )
        
        context = {
            "form": form,
            "title": title,
            "submit_text": submit_text,
        }
        
        return render(
            request,
            "activity/new.html",
            context,
        )
        
    def post(self, request, pk):
        form = AddActivity(request.POST)
        
        if form.is_valid():
            form.save()
            
            context={
                "form": form,
                "success": "Activité modifiée avec succès.",
            }
            
            return redirect("activity")
        else:
            print(form.errors)
            
            context={
                "form": form,
                "errors": form.errors,
            }
            
            return render(
                request,
                "activity/new.html",
                context
            )
            
class ActivityDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        activity = get_object_or_404(Activity, pk=pk)
        activity.delete()
        
        return redirect("activity")