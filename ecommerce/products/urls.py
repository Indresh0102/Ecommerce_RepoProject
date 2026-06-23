from django.urls import path, include
from .views import greet_user
urlpatterns = [
    path('greet/', greet_user, name='greeting'),
]