from django.urls import path
from .views import TripView, TripDetail, NewTrip, TripUpdate, TripDelete

urlpatterns = [
    path("", TripView.as_view(), name="trip"),
    path("ajouter/", NewTrip.as_view(), name="trip_new"),
    path("<int:pk>/", TripDetail.as_view(), name="trip_detail"),
    path("<int:pk>/modifier/", TripUpdate.as_view(), name="trip_update"),
    path("<int:pk>/supprimer/", TripDelete.as_view(), name="trip_delete"),
]
