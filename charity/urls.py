from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.home, name="index"),
    path("charity/add_charity", views.add_charity, name="add_charity"),
    path("charity/choose_charity", views.search_charity, name="search_charity"),
    path("charity/update_charity/<id>", views.edit_charity, name="edit_charity"),
]