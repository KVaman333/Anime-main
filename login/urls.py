from django.urls import path
from .views      import *



urlpatterns = [
    path('', domain, name='domain'),
    path('authentication/login/', login, name='login'),
    path('authentication/logout/', logout, name='logout'),
]
