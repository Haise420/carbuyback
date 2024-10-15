from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('usluge', views.usluge, name="usluge"),
    path('novosti', views.novosti, name="novosti"),
    path('kontakt', views.kontakt, name="kontakt"),
]