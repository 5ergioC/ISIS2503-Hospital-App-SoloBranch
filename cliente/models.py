import hashlib
from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)  # Nuevo campo email
    phone = models.CharField(max_length=20, blank=True, null=True)    # Nuevo campo teléfono
    address = models.TextField(blank=True, null=True)                 # Nuevo campo dirección
    hash_integridad = models.CharField(max_length=64, editable=False, blank=True)

    def save(self, *args, **kwargs):
        self.hash_integridad = self.generar_hash()
        super().save(*args, **kwargs)

    def generar_hash(self):
        # Incluye nuevos campos en el hash para asegurar integridad completa
        valores = f"{self.name}|{self.email or ''}|{self.phone or ''}|{self.address or ''}"
        return hashlib.sha256(valores.encode()).hexdigest()

    def verificar_integridad(self):
        return self.hash_integridad == self.generar_hash()

    def __str__(self):
        return f'{self.name}'
