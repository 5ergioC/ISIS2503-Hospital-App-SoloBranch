from ..models import Cliente

def get_clientes():
    queryset = Cliente.objects.all()
    return (queryset)

def create_cliente(form):
    measurement = form.save()
    measurement.save()
    return ()