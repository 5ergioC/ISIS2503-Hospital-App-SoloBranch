from ..models import Cliente

def get_clientes():
    clientes = Cliente.objects.all()
    for cliente in clientes:
        if not cliente.verificar_integridad():
            print(f'¡Alerta! Cliente con ID {cliente.id} tiene datos modificados.')
    return clientes

def create_cliente(form):
    cliente = form.save(commit=False)
    cliente.save()
    return cliente