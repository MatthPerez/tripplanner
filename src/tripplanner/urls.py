from django.contrib import admin
from django.urls import path, include

from .views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home.as_view(), name="home"),
    path("airbnb/", include("airbnb.urls")),
    path("trajet/", include("travel.urls")),
    path("activite/", include("activity.urls")),
    path("depense/", include("expense.urls")),
    path("voyage/", include("trip.urls")),
    path("destination/", include("country.urls")),
    path("experiences/", include("experiences.urls")),

]
