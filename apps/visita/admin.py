from django import forms
from django.contrib import admin
from django.forms.widgets import RadioSelect

from .models import Visita

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'
        widgets = {
            'estado': RadioSelect,
        }

class VisitaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'email', 'direccion', 'servicio', 'fecha_solicitud', 'estado', 'fecha_atendido']
    list_filter = ['estado']
    search_fields = ['id', 'cliente']
    readonly_fields = ['id']
    fieldsets = [
        ('Información de la Visita', {
            'fields': ['id', 'cliente', 'email', 'direccion', 'servicio', 'fecha_solicitud', 'estado', 'fecha_atendido']
        }),
        ('Detalles Adicionales', {
            'fields': ['notas', 'responsable', 'location']
        }),
    ]

admin.site.register(Visita, VisitaAdmin)
