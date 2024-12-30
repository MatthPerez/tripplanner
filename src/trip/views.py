from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import FormView
from django.views import View
from django.views.generic import DetailView
from .forms import AddTrip
from .models import Trip
from activity.models import Activity
from airbnb.models import Airbnb
from expense.models import Expense
from django.utils.timezone import now
# from tripplanner.static.scripts.scrap import wikipedia

# from django.contrib.auth.mixins import UserPassesTestMixin


# def is_admin(user):
#     return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class TripView(View):
    def get(self, request):
        today = now()
        trips = Trip.objects.filter(
            date__gte=today,
        ).order_by("date")

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

        country = context["trip"].place
        context["place"] = country
        context["travels"] = context["trip"].travels.all()
        context["airbnbs"] = context["trip"].airbnbs.all()
        context["activities"] = context["trip"].activities.all()
        context["expenses"] = context["trip"].expenses.all()
        context["total_price"] = context["trip"].total_price

        # context["wikipedia_paragraphs"] = wikipedia(country)

        return context


class NewTrip(View):
    def get(self, request, pk=None):
        if pk:
            trip = get_object_or_404(Trip, pk=pk)
            form = AddTrip(instance=trip)
            title = "Modifier un voyage"
            submit_text = "Modifier"
        else:
            form = AddTrip()
            title = "Ajouter un voyage"
            submit_text = "Ajouter"

        all_expenses = list(Expense.objects.values_list("id", "name", "price"))

        airbnbs_with_destination = []

        for airbnb in Airbnb.objects.all():
            destination = airbnb.country.name
            
            if destination:
                airbnbs_with_destination.append(
                    {"id": airbnb.id, "name": f"{airbnb.name} ({destination})"}
                )
            else:
                airbnbs_with_destination.append({"id": airbnb.id, "name": airbnb.name})

        activities_with_destination = []

        for activity in Activity.objects.all():
            destination = (
                activity.countries.first().name if activity.countries.exists() else None
            )
            if destination:
                activities_with_destination.append(
                    {"id": activity.id, "name": f"{activity.name} ({destination})"}
                )
            else:
                activities_with_destination.append(
                    {"id": activity.id, "name": activity.name}
                )

        context = {
            "form": form,
            "title": title,
            "submit_text": submit_text,
            "activities_with_destination": activities_with_destination,
            "airbnbs_with_destination": airbnbs_with_destination,
            "all_expenses": all_expenses,
        }

        return render(request, "trip/new.html", context)

    def post(self, request, pk=None):
        if pk:
            trip = get_object_or_404(Trip, pk=pk)
            form = AddTrip(request.POST, instance=trip)
        else:
            form = AddTrip(request.POST)

        if form.is_valid():
            trip = form.save()

            selected_expenses = form.cleaned_data["expenses"]
            trip.expenses.set(selected_expenses)

            return redirect("trip_detail", pk=trip.pk)
        else:
            print(form.errors)  # Pour le débogage

            context = {
                "form": form,
                "errors": form.errors,
            }

            return render(request, "trip/new.html", context)


class TripUpdate(FormView):
    template_name = "trip/new.html"
    form_class = AddTrip

    def get_initial(self):
        initial = super().get_initial()
        trip = get_object_or_404(Trip, pk=self.kwargs["pk"])

        initial.update(
            {
                "date": trip.date.strftime("%Y-%m-%d"),
                "duration": trip.duration,
                "people": trip.people,
                "place": (trip.place.name if trip.place else None),
            }
        )

        print(f"ID destination : {trip.place.id}")

        for field_name in ["travels", "airbnbs", "activities", "expenses"]:
            related_objects = getattr(trip, field_name).all()
            initial[field_name] = [obj.id for obj in related_objects]

        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Mise à jour du voyage"
        context["submit_text"] = "Enregistrer"

        trip = get_object_or_404(Trip, pk=self.kwargs["pk"])

        airbnbs_with_destination = []

        for airbnb in Airbnb.objects.all():
            destination = airbnb.country.name
            
            if destination:
                airbnbs_with_destination.append(
                    {"id": airbnb.id, "name": f"{airbnb.name} ({destination})"}
                )
            else:
                airbnbs_with_destination.append({"id": airbnb.id, "name": airbnb.name})

        activities_with_destination = []

        for activity in Activity.objects.all():
            destination = (
                activity.countries.first().name if activity.countries.exists() else None
            )
            if destination:
                activities_with_destination.append(
                    {"id": activity.id, "name": f"{activity.name} ({destination})"}
                )
            else:
                activities_with_destination.append(
                    {"id": activity.id, "name": activity.name}
                )

        all_expenses = list(Expense.objects.values_list("id", "name", "price"))
        expenses_ids = list(trip.expenses.values_list("id", flat=True))

        # print(f"All expenses: {all_expenses}")
        # print(f"Expenses IDs: {expenses_ids}")

        context["airbnbs_with_destination"] = airbnbs_with_destination
        context["activities_with_destination"] = activities_with_destination
        context["all_expenses"] = all_expenses
        context["airbnbs_ids"] = list(trip.airbnbs.values_list("id", flat=True))
        context["activities_ids"] = list(trip.activities.values_list("id", flat=True))
        context["expenses_ids"] = expenses_ids

        return context

    def form_valid(self, form):
        trip = get_object_or_404(Trip, pk=self.kwargs["pk"])
        form.instance = trip

        trip.date = form.cleaned_data["date"]
        trip.duration = form.cleaned_data["duration"]
        trip.place = form.cleaned_data["place"]
        trip.people = form.cleaned_data["people"]

        trip.airbnbs.set(form.cleaned_data["airbnbs"])
        trip.activities.set(form.cleaned_data["activities"])
        trip.expenses.set(form.cleaned_data["expenses"])

        trip.save()

        return redirect("trip_detail", pk=trip.pk)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form, errors=form.errors)
        )


class TripDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        trip = get_object_or_404(Trip, pk=pk)
        trip.delete()

        return redirect("trip")
