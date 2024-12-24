from django.urls import path
from .views import Airbnb, NewAirbnb

urlpatterns = [
    path("", Airbnb.as_view(), name="airbnb"),
    path("ajouter/", NewAirbnb.as_view(), name="airbnb_new"),
    # path("<int:pk>/modifier/", UpdateAirbnb.as_view(), name="airbnb_update"),
    # path("<int:pk>/supprimer/", DeleteAirbnb.as_view(), name="airbnb_delete"),
]
