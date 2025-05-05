import hashlib
from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length=50)
    data_hash = models.CharField(max_length=64, editable=False, blank=True)

    def save(self, *args, **kwargs):
        self.hash_integridad = self.generar_hash()
        super().save(*args, **kwargs)

    def generar_hash(self):
        return hashlib.sha256(self.name.encode()).hexdigest()

    def verificar_integridad(self):
        return self.hash_integridad == self.generar_hash()


    def __str__(self):
        return '{}'.format(self.name)

