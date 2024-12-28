from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from .forms import AddActivity
from .models import Activity
# from django.contrib.auth.mixins import UserPassesTestMixin


# def is_admin(user):
#     return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class ActivityView(View):
    def get(self, request):
        activities = Activity.objects.prefetch_related('cities').order_by("name")
        
        context = {
            "activities": activities,
        }
        
        return render(
            request,
            "activity/index.html",
            context,
        )
        
class ActivityDetail(DetailView):
    model = Activity
    template_name=  "activity/detail.html"
    context_object_name = "activity"

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
        title = "Mise à jour de l'activité"
        submit_text = "Enregistrer"
        
        form = AddActivity(instance=activity)
        
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
        activity = Activity.objects.get(pk=pk)
        
        form = AddActivity(request.POST, instance=activity)
        
        if form.is_valid():
            form.save()
            
            context = {
                "form": form,
                "success": "Activité modifiée avec succès.",
            }
            
            return redirect("activity")
        else:
            print(form.errors)
            
            context = {
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