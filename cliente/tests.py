from django.test import TestCase
from .models import Cliente

class IntegridadClienteTest(TestCase):
    def test_cliente_integridad_valida(self):
        cliente = Cliente.objects.create(name="Pedro")
        self.assertTrue(cliente.verificar_integridad())

    def test_cliente_integridad_corrupta(self):
        cliente = Cliente.objects.create(name="Pedro")
        cliente.hash_integridad = "valor_invalido"
        self.assertFalse(cliente.verificar_integridad())
