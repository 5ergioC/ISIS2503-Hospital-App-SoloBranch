from collections import Counter
from ..models import MRI, Cliente

def get_mris():
    mris = MRI.objects.all()
    return mris

def get_mri(user_pk):
    mri = MRI.objects.filter(cliente=user_pk).order_by('-fecha', '-hora').first()
    return mri

def update_mri(mri_pk, new_data):
    try:
        mri = MRI.objects.get(pk=mri_pk) 
        mri.descripcion = new_data.get("descripcion", mri.descripcion)
        mri.fecha = new_data.get("fecha", mri.fecha)
        mri.hora = new_data.get("hora", mri.hora)
        mri.save()
        return mri
    except MRI.DoesNotExist:
        return None

def create_mri(form):
    measurement = form.save()
    measurement.save()
    return ()

def map_reduce_usuarios():
    usuarios_ids = MRI.objects.values_list('cliente', flat=True)

    conteo_usuarios = Counter(usuarios_ids)

    usuarios_ordenados = sorted(conteo_usuarios.items(), key=lambda item: item[1], reverse=True)

    return usuarios_ordenados

def get_usuario_mas_atendido():
    usuarios_ordenados = map_reduce_usuarios()

    if usuarios_ordenados:
        user_id, cantidad = usuarios_ordenados[0]  
        cliente = Cliente.objects.get(id=user_id)
        return {"cliente": cliente, "cantidad": cantidad}
    return None

def get_5_usuarios_mas_atendido():
    usuarios_ordenados = map_reduce_usuarios()

    if usuarios_ordenados:
        usuarios = []
        for user_id, cantidad in usuarios_ordenados[:5]: #esto va para los filtros, la idea es como poner un filtro con los 5 usuarios mas atendidos o no se si poner todos la vd
            cliente = Cliente.objects.get(id=user_id)
            usuarios.append({"cliente": cliente, "cantidad": cantidad})
        return usuarios
    return None

