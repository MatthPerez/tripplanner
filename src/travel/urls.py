from django.urls import path
from .views import TravelView, NewTravel, TravelUpdate, TravelDelete

urlpatterns = [
    path("", TravelView.as_view(), name="travel"),
    path("ajouter/", NewTravel.as_view(), name="travel_new"),
    path("<int:pk>/modifier/", TravelUpdate.as_view(), name="travel_update"),
    path("<int:pk>/supprimer/", TravelDelete.as_view(), name="travel_delete"),
]
