from django.urls import path
from .views import ActivityView, ActivityDetail, NewActivity, ActivityUpdate, ActivityDelete

urlpatterns = [
    path("", ActivityView.as_view(), name="activity"),
    path("ajouter/", NewActivity.as_view(), name="activity_new"),
    path("<int:pk>/", ActivityDetail.as_view(), name="activity_detail"),
    path("<int:pk>/modifier/", ActivityUpdate.as_view(), name="activity_update"),
    path("<int:pk>/supprimer/", ActivityDelete.as_view(), name="activity_delete"),
]
