from django.urls import path
from .views import CountryView, NewCountry, CountryUpdate, CountryDelete

urlpatterns = [
    path("", CountryView.as_view(), name="country"),
    path("ajouter/", NewCountry.as_view(), name="country_new"),
    path("<int:pk>/modifier/", CountryUpdate.as_view(), name="country_update"),
    path("<int:pk>/supprimer/", CountryDelete.as_view(), name="country_delete"),
]
