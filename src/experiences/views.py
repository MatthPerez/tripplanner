from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from .forms import AddExperience
from .models import Experience
from tripplanner.static.scripts.scrap import experiments

# from django.contrib.auth.mixins import UserPassesTestMixin


# def is_admin(user):
#     return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class ExperienceView(View):
    def get(self, request):
        pics = experiments()
        experiences = Experience.objects.order_by('name')

        context = {
            "pics": pics,
            "experiences": experiences,
        }

        return render(
            request,
            "experiences/index.html",
            context,
        )


class ExperienceDetail(DetailView):
    model = Experience
    template_name = "experiences/detail.html"
    context_object_name = "experience"


class NewExperience(View):
    def get(self, request):
        form = AddExperience()
        title = "Ajouter une expérience"
        submit_text = "Ajouter"

        context = {
            "form": form,
            "title": title,
            "submit_text": submit_text,
        }

        return render(
            request,
            "experiences/new.html",
            context,
        )

    def post(self, request):
        form = AddExperience(request.POST)

        if form.is_valid():
            form.save()

            return redirect("experience")
        else:
            print(form.errors)

            context = {
                "form": form,
                "errors": form.errors,
            }

            return render(request, "experiences/new.html", context)


class ExperienceUpdate(View):
    def get(self, request, pk):
        experience = Experience.objects.get(pk=pk)
        title = "Mise à jour de l'expérience"
        submit_text = "Enregistrer"

        form = AddExperience(instance=experience)

        context = {
            "form": form,
            "title": title,
            "submit_text": submit_text,
        }

        return render(
            request,
            "experiences/new.html",
            context,
        )

    def post(self, request, pk):
        experience = Experience.objects.get(pk=pk)

        form = AddExperience(
            request.POST,
            instance=experience,
        )

        if form.is_valid():
            form.save()

            return redirect("experience")
        else:
            print(form.errors)

            context = {
                "form": form,
                "errors": form.errors,
            }

            return render(request, "experiences/new.html", context)


class ExperienceDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        experience = get_object_or_404(Experience, pk=pk)
        experience.delete()

        return redirect("experience")
