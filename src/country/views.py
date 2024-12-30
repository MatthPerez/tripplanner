from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from .forms import AddCountry
from .models import Country
from tripplanner.static.scripts.scrap import wikipedia

# from django.contrib.auth.mixins import UserPassesTestMixin


# def is_admin(user):
#     return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class CountryView(View):
    def get(self, request):
        countries = Country.objects.order_by("name")

        context = {
            "countries": countries,
        }

        return render(
            request,
            "country/index.html",
            context,
        )


class CountryDetail(DetailView):
    model = Country
    template_name = "country/detail.html"
    context_object_name = "country"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["name"] = context["country"].name
        context["wikipedia_lines"] = wikipedia(context["name"])

        return context


class NewCountry(View):
    def get(self, request):
        form = AddCountry()
        title = "Ajouter une destination"
        submit_text = "Ajouter"

        context = {
            "form": form,
            "title": title,
            "submit_text": submit_text,
        }

        return render(
            request,
            "country/new.html",
            context,
        )

    def post(self, request):
        form = AddCountry(request.POST)

        if form.is_valid():
            form.save()

            context = {
                "form": form,
                "success": "Destination ajoutée avec succès.",
            }

            return redirect("country")
        else:
            print(form.errors)

            context = {
                "form": form,
                "errors": form.errors,
            }

            return render(request, "country/new.html", context)


class CountryUpdate(View):
    def get(self, request, pk):
        country = Country.objects.get(pk=pk)
        title = f"Mise à jour de la destination"
        submit_text = "Enregistrer"

        form = AddCountry(
            instance=country,
            initial={
                "name": country.name,
            },
        )

        context = {
            "form": form,
            "title": title,
            "submit_text": submit_text,
        }

        return render(
            request,
            "country/new.html",
            context,
        )

    def post(self, request, pk):
        country = Country.objects.get(pk=pk)
        form = AddCountry(request.POST, instance=country)

        if form.is_valid():
            form.save()

            context = {
                "form": form,
                "success": "Destination modifiée avec succès.",
            }

            return redirect("country")
        else:
            print(form.errors)

            context = {
                "form": form,
                "errors": form.errors,
            }

            return render(request, "country/new.html", context)


class CountryDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        country = get_object_or_404(Country, pk=pk)
        country.delete()

        return redirect("country")
