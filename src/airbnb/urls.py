from django.urls import path
from .views import AirbnbView, NewAirbnb, AirbnbUpdate, AirbnbDelete

urlpatterns = [
    path("", AirbnbView.as_view(), name="airbnb"),
    path("ajouter/", NewAirbnb.as_view(), name="airbnb_new"),
    path("<int:pk>/modifier/", AirbnbUpdate.as_view(), name="airbnb_update"),
    path("<int:pk>/supprimer/", AirbnbDelete.as_view(), name="airbnb_delete"),
]
