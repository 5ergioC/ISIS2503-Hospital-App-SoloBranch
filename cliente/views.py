from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
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