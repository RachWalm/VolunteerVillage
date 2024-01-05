from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.home, name="index"),
    path("coordinator/pending", views.pending, name="pending"),
    path("coordinator/dashboard", views.dashboard, name="dashboard"),
    path("coordinator/add_profile", views.add_profile_co, name="addco"),
    path("coordinator/update_profile/<id>", views.edit_profile_co, name="updateco"),
    path("coordinator/choose_profile", views.search_coordinators, name="searchco"),
    path("coordinator/see_profile/<id>", views.read_coordinator, name="readco"),
    path("coordinator/delete_profile/<id>", views.delete_profile_co, name="deleteco"),
    path("coordinator/search_volunteer", views.search_volunteer, name="searchvol"),
]