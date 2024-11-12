from django.urls import path
from .views import profile, profile_view

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile/<str:username>/', profile_view, name='profile_view'),
]
