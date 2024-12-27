from django.shortcuts import render
from django.views import View
from trip.models import Trip
from .static.scripts.scrap import kayak, verychic

# from django.contrib.auth.mixins import UserPassesTestMixin


# def is_admin(user):
#     return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class Home(View):
    def get(self, request):
        kayak_elements = kayak()
        verychic_elements = verychic()

        trips = Trip.objects.order_by("place", "date")

        context = {
            "kayak_elements": kayak_elements,
            "verychic_elements": verychic_elements,
            "trips": trips,
        }

        return render(
            request,
            "tripplanner/index.html",
            context,
        )
