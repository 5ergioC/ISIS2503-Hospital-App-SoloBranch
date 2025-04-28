from django.db import models

from cliente.models import Cliente
# Create your models here.
class MRI(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField(default="Sin descripcion")

    def __str__(self):
        return '%s %s' % (self.cliente, self.descripcion)