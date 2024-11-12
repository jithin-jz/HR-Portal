from django.urls import path
from . import views

urlpatterns = [
    path("employe/", views.employe, name="employe"),
]