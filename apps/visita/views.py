from typing import Any
from django import http
from django.http import JsonResponse
from django.utils.decorators import method_decorator 
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views import View
from .models import Visita
import json
import uuid
# Create your views here.
class VisitaView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=None):
        if id:
            try:
                uuid_obj = uuid.UUID(id)
                visitas = list(Visita.objects.filter(id=str(uuid_obj)).values())
                if len(visitas) > 0:
                    visita = visitas[0]
                    datos =  visita
                else:
                    datos = {'message': "Visita no encontrada..."}
            except ValueError:
                datos = {'message': "Invalid UUID format"}
        else:
            visitas = list(Visita.objects.values())
            if len(visitas) > 0:
                datos =  visitas
            else:
                datos = {'message': "No se encontró información"}
        
        return JsonResponse(datos, safe=False)
    
    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Visita.objects.create(
            cliente=jd['cliente'],
            email=jd['email'],
            direccion=jd['direccion'],
            servicio=jd['servicio'], 
            fecha_solicitud=jd['fecha_solicitud'],
            estado=jd['estado'],
            fecha_atendido=jd['fecha_atendido'],
            notas=jd['notas'], 
            responsable=jd['responsable'], 
            location=jd['location'],
            )
        datos={'message':"Success"}

        return JsonResponse(datos)
    
    def put(self, request, id=None):
        jd = json.loads(request.body)
        if id:
            try:
                uuid_obj = uuid.UUID(id)
                visitas = list(Visita.objects.filter(id=str(uuid_obj)).values()) 
                if len(visitas) > 0:
                    visita = Visita.objects.get(id=id)
                    visita.cliente = jd['cliente']
                    visita.email = jd['email']
                    visita.direccion = jd['direccion']
                    visita.servicio=jd['servicio'] 
                    visita.fecha_solicitud=jd['fecha_solicitud']
                    visita.estado=jd['estado']
                    visita.fecha_atendido=jd['fecha_atendido']
                    visita.notas=jd['notas']
                    visita.responsable=jd['responsable']
                    visita.location=jd['location']
                    
                    visita.save()
                    datos = {'message': "Success"}
                else:
                    datos = {'message': "Visita no encontrado..."}
            except ValueError:
                datos = {'message': "Invalid UUID format"}
        else:
            visitas = list(Visita.objects.values())
            if len(visitas) > 0:
                datos = {'message': "Exitoso", 'visitas': visitas}
            else:
                datos = {'message': "No se encontró información"}
        
        return JsonResponse(datos)

    
    def delete(self, request,id=None):
        if id:
            try:
                uuid_obj = uuid.UUID(id)
                visitas = list(Visita.objects.filter(id=str(uuid_obj)).values())
                if len(visitas) > 0:
                    Visita.objects.filter(id=id).delete()
                    datos = {'message': "Success"}
                else:
                    datos = {'message': "Visita no encontrado..."}
            except ValueError:
                datos = {'message': "Invalid UUID format"}
        else:
            visitas = list(Visita.objects.values())
            if len(visitas) > 0:
                datos = {'message': "Exitoso", 'visitas': visitas}
            else:
                datos = {'message': "No se encontró información"}
        
        return JsonResponse(datos)
