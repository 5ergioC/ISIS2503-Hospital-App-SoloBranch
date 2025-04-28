from django.shortcuts import render
from .forms import MRIForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_MRI import create_mri, get_mri

def MRI_list(request):
    user_pk = request.GET.get('cliente_id') 
    
    if not user_pk:
        return render(request, 'MRI/MRI.html', {'error': 'Es necesario una llave foranea de los clientes'})

    MRI = get_mri(user_pk)
    print(f"Datos de MRI para user_pk {user_pk}: {MRI}")
    
    context = {
        'MRI_list': MRI
    }
    return render(request, 'MRI/MRI.html', context)

def MRI_create(request):
    if request.method == 'POST':
        form = MRIForm(request.POST)
        if form.is_valid():
            create_mri(form)
            messages.add_message(request, messages.SUCCESS, 'MRI create successful')
            return HttpResponseRedirect(reverse('MRICreate'))
        else:
            print(form.errors)
    else:
        form = MRIForm()

    context = {
        'form': form,
    }

    return render(request, 'MRI/MRICreate.html', context)