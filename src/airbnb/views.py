from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic.edit import FormView
from .forms import AddAirbnb
from .models import Airbnb
from django.utils.timezone import now

# from django.contrib.auth.mixins import UserPassesTestMixin


# def is_admin(user):
#     return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class AirbnbView(View):
    def get(self, request):
        today = now()
        airbnbs = (
            Airbnb.objects.prefetch_related("countries")
            .filter(
                start_date__gte=today,
            )
            .order_by("name")
        )

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
        title = "Ajouter un logement"
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

            context = {
                "form": form,
                "success": "Logement ajouté avec succès.",
            }

            return redirect("airbnb")
        else:
            print(form.errors)

            context = {
                "form": form,
                "errors": form.errors,
            }

            return render(request, "airbnb/new.html", context)


class AirbnbUpdate(FormView):
    template_name = "airbnb/new.html"
    form_class = AddAirbnb

    def get_initial(self):
        initial = super().get_initial()
        airbnb = get_object_or_404(Airbnb, pk=self.kwargs["pk"])

        initial.update(
            {
                "name": airbnb.name,
                "countries": list(
                    airbnb.countries.values_list("id", flat=True)
                ),
                "reference": airbnb.reference,
                "price": airbnb.price,
                "charges": airbnb.charges,
                "start_date": airbnb.start_date.strftime("%Y-%m-%d"),
                "end_date": airbnb.end_date.strftime("%Y-%m-%d"),
            }
        )

        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Mise à jour du voyage"
        context["submit_text"] = "Enregistrer"
        return context

    def form_valid(self, form):
        airbnb = get_object_or_404(Airbnb, pk=self.kwargs["pk"])
        # form.instance = airbnb

        airbnb.name = form.cleaned_data["name"]
        airbnb.reference = form.cleaned_data["reference"]
        airbnb.price = form.cleaned_data["price"]
        airbnb.charges = form.cleaned_data["charges"]
        airbnb.start_date = form.cleaned_data["start_date"]
        airbnb.end_date = form.cleaned_data["end_date"]

        airbnb.save()

        airbnb.countries.set(form.cleaned_data["countries"])

        return redirect("airbnb_detail", pk=airbnb.pk)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form, errors=form.errors)
        )


class AirbnbDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        airbnb = get_object_or_404(Airbnb, pk=pk)
        airbnb.delete()

        return redirect("airbnb")
