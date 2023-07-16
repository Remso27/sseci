from django.urls import path
from django.views.generic.base import RedirectView
from . import views


app_name = 'web'

urlpatterns = [
    path('', views.accueil, name='accueil'),
]