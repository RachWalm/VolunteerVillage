from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.home, name="index"),
    path("volunteer/add_profile", views.add_profile, name="add"),
    path("volunteer/read_profile", views.read_profile, name="read"),
    path("volunteer/edit_profile", views.edit_profile, name="edit"),
    path("volunteer/delete_profile", views.delete_profile, name="delete"),
]
