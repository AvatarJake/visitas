import requests
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
import uuid
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

class Visita(models.Model):
    estados = (
        ('pendiente', 'Pendiente'),
        ('en proceso', 'En Proceso'),
        ('operado', 'Operado'),
        ('cancelado','Cancelado'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.CharField('Cliente', max_length=100, blank=True, null=True)
    email = models.CharField('email', max_length=100, blank=True, null=True)
    direccion= models.CharField('Dirección', max_length=200, blank=True, null=True)
    servicio = models.CharField('Servicio', max_length=100, blank=True, null=True)
    fecha_solicitud = models.DateField('Fecha de Solicitud', null=True, blank=True)
    estado = models.CharField(max_length=100, choices=estados, default='Pendiente')
    fecha_atendido = models.DateField('Fecha de Atendido', null=True, blank=True)
    notas = models.TextField(blank=True, null=True)
    responsable = models.CharField('Tecnico Responsable', max_length=100, blank=True, null=True)
    location = models.CharField('Ubicacion', max_length=100, blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     if self.estado == 'operado':
    #         msg = MIMEMultipart()
    #         direccionenvio = 'skynet.syscontact@yahoo.com'
    #         destino = self.email
    #         msg['From'] = direccionenvio
    #         msg['To'] = self.email
    #         msg['Subject'] = 'Visita Finalizada'

    #         html_body = f'''
    #                 <html>
    #                     <head></head>
    #                     <body>
    #                     <h1>Hola, se ha Finaliado el trabajo programado</h1>
    #                     <p>Tipo de Trabajo: {self.servicio}</p>
    #                     <p>Fecha de Solicitud: {self.fecha_solicitud}</p>
    #                     <p>Fecha de atencion: {self.fecha_atendido}</p>
    #                     <p>Notas: {self.notas}</p><br><br>
    #                     <p> Agradecemos mucho su confianza en nosotros, que tengas un bendecido dia!!</p>
    #                     </body>
    #                 </html>
    #                         '''
    #         msg.attach(MIMEText(html_body, 'html'))
    #         smtp_server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    #         smtp_server.ehlo()
    #         smtp_server.starttls()
    #         smtp_server.login('skynet.syscontact@yahoo.com', '091089nj')
    #         text = msg.as_string()
    #         smtp_server.sendmail(direccionenvio, destino, text)
    #         smtp_server.quit()

    #         print("El correo fue enviado!")

    #     super().save(*args, **kwargs)