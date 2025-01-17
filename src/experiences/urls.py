from django.urls import path
from .views import (
    ExperienceView,
    ExperienceDetail,
    NewExperience,
    ExperienceUpdate,
    ExperienceDelete,
)

urlpatterns = [
    path("", ExperienceView.as_view(), name="experience"),
    path("ajouter/", NewExperience.as_view(), name="experience_new"),
    path("<int:pk>/", ExperienceDetail.as_view(), name="experience_detail"),
    path("<int:pk>/modifier/", ExperienceUpdate.as_view(), name="experience_update"),
    path("<int:pk>/supprimer/", ExperienceDelete.as_view(), name="experience_delete"),
]
