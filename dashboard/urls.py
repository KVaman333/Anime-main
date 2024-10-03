from login.views import domain
from django.urls import path
from .views      import *



urlpatterns = [
    path('homepage/',homepage, name='homepage'),
    path('watch/<str:anime>/',watch, name='watch'),
]
