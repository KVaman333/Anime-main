from django.urls import path
from .views.watch import switch_ep


urlpatterns = [ #  HEADER == ajaxhandler/
    path('switch-episode/', switch_ep)
]

