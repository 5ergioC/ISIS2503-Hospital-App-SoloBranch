from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'name',
            'email',
            'phone',
            'address',
        ]
        labels = {
            'name': 'Nombre',
            'email': 'Correo Electrónico',
            'phone': 'Teléfono',
            'address': 'Dirección',
        }
