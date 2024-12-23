from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from django.views import View
# from django.contrib.auth.mixins import UserPassesTestMixin


# def is_admin(user):
#     return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class Home(View):
    def get(self, request):
        return render(
            request,
            "tripplanner/index.html",
        )