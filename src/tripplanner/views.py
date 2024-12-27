from django.shortcuts import render
from django.views import View
from trip.models import Trip
from .static.scripts.scrap import kayak, staycation

# from django.contrib.auth.mixins import UserPassesTestMixin


# def is_admin(user):
#     return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class Home(View):
    def get(self, request):
        kayak_elements = kayak()
        staycation_elements = staycation("45.764%2C4.83566")

        trips = Trip.objects.order_by("place", "date")

        context = {
            "kayak_elements": kayak_elements,
            "staycation_elements": staycation_elements,
            "trips": trips,
        }

        return render(
            request,
            "tripplanner/index.html",
            context,
        )
