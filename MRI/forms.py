from django import forms

class MRIForm(forms.Form):
    cliente = forms.CharField(label="Cliente")
    fecha = forms.DateField(label="Fecha")
    hora = forms.TimeField(label="Hora")
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripción")
    imagen_url = forms.URLField(label="URL Imagen", required=False)  # nuevo campo
