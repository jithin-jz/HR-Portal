from django.urls import path
from . import views

urlpatterns = [
    path('expenses/', views.manage_expenses, name='manage_expenses'),
]
