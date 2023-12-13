from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.home, name="index"),
    path("role/role", views.role, name="role"),
    path('login_success', views.login_success, name='login_success')
]