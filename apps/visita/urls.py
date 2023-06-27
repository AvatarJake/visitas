from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('visitas/',VisitaView.as_view(),name='visitas_list'),
    path('visitas/<str:id>',VisitaView.as_view(),name='visitas_process'),
    path('visitas/<str:id>/change/',VisitaView.as_view(),name='visitas_puts'),
]
