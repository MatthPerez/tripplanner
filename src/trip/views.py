from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import FormView
from django.views import View
from django.views.generic import DetailView
from .forms import AddTrip
from .models import Trip
from django.utils.timezone import now
from tripplanner.static.scripts.scrap import wikipedia
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

        context["country"] = context["trip"].place
        context["travels"] = context["trip"].travels.all()
        context["airbnbs"] = context["trip"].airbnbs.all()
        context["activities"] = context["trip"].activities.all()
        context["expenses"] = context["trip"].expenses.all()
        context["total_price"] = context["trip"].total_price

        city = context["trip"].place
        context["wikipedia_paragraphs"] = wikipedia(city)

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

class TripUpdate(FormView):
    template_name = 'trip/new.html'
    form_class = AddTrip

    def get_initial(self):
        initial = super().get_initial()
        trip = get_object_or_404(Trip, pk=self.kwargs['pk'])
        initial.update({
            'date': trip.date.strftime("%Y-%m-%d"),
            'duration': trip.duration,
            'place': trip.place,
            'people': trip.people,
        })
        for field_name in ['country', 'travels', 'airbnbs', 'activities', 'expenses']:
            related_objects = getattr(trip, field_name).all()
            initial[field_name] = [obj.id for obj in related_objects]
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Mise à jour du voyage"
        context['submit_text'] = "Enregistrer"
        
        return context

    def form_valid(self, form):
        trip = get_object_or_404(Trip, pk=self.kwargs['pk'])
        form.instance = trip
        form.save()
        
        return redirect('trip_detail', pk=trip.pk)


    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form, errors=form.errors))

class TripDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        trip = get_object_or_404(Trip, pk=pk)
        trip.delete()
        
        return redirect("trip")
