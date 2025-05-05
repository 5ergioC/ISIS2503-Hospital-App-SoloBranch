from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from .forms import ClienteForm
from .logic.cliente_logic import get_clientes, create_cliente
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

@login_required
def cliente_list(request):
    clientes = get_clientes()
    context = {
        'cliente_list': clientes
    }
    return render(request, 'cliente/clientes.html', context)

    

@login_required
def cliente_create(request):
    role = getRole(request)
    if role == "Medico":
        if request.method == 'POST':
            form = ClienteForm(request.POST)
            if form.is_valid():
                create_cliente(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created cliente')
                return HttpResponseRedirect(reverse('clienteCreate'))
            else:
                print(form.errors)
        else:
            form = ClienteForm()

        context = {
            'form': form,
        }
        return render(request, 'cliente/clienteCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")
    
@login_required
def cliente_integrity_check(request):
    role = getRole(request)
    if role == "Medico":
        clientes = get_clientes()
        return render(request, 'cliente/clientesIntegridad.html', {'clientes': clientes})
    else:
        return HttpResponse("Unauthorized User")

@login_required
def verificar_integridad_view(request):
    role = getRole(request)
    if role == "Medico":
        total = 0
        corruptos = 0
        registros_corruptos = []
        clientes = get_clientes()
        for cliente in clientes:
            total += 1
            if not cliente.verificar_integridad():
                corruptos += 1
                registros_corruptos.append({
                    "id": cliente.id,
                    "name": cliente.name,
                    "hash_guardado": cliente.hash_integridad,
                    "hash_esperado": cliente.generar_hash(),
                })

        return JsonResponse({
            "total_registros": total,
            "registros_corruptos": corruptos,
            "porcentaje_corruptos": (corruptos / total) * 100 if total else 0,
            "detalles": registros_corruptos,
        })
    else:
        return HttpResponse("Unauthorized User")