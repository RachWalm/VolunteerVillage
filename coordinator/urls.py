from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.home, name="index"),
    path("coordinator/pending", views.pending, name="pending"),
]