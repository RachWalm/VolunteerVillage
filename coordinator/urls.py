from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.home, name="index"),
    path("coordinator/pending", views.pending, name="pending"),
    path("coordinator/dashboard", views.dashboard, name="dashboard"),
    path("coordinator/add_profile", views.add_profile_co, name="addco"),
]