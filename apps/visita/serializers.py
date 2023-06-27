from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Visita
        fields=[
            'id',
            'cliente',
            'servicio',
            'fecha_solicitud',
            'estado',
            'fecha_atendido',
            'notas',
            'responsable',
            'location',
            'punto_partida',
        ]