from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Paciente
from .forms import PacienteForm

# Create your views here.
def index(request):
    return render(request, 'pacientes/index.html',{
        'pacientes': Paciente.objects.all()
    })

def view_paciente(request, id):
    paciente = Paciente.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            new_id_pac = form.cleaned_data['id_pac']
            new_nombre_pac = form.cleaned_data['nombre_pac']
            new_apellido_pac = form.cleaned_data['apellido_pac']
            new_fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            new_telefono_pac = form.cleaned_data['telefono_pac']
            new_direccion_pac = form.cleaned_data['direccion_pac']
            new_correo_pac = form.cleaned_data['correo_pac']
            new_fecha_registro = form.cleaned_data['fecha_registro']
        
            new_paciente = Paciente(
                id_pac = new_id_pac,
                nombre_pac = new_nombre_pac,
                apellido_pac = new_apellido_pac,
                fecha_nacimiento = new_fecha_nacimiento,
                telefono_pac = new_telefono_pac,
                direccion_pac = new_direccion_pac,
                correo_pac = new_correo_pac,
                fecha_registro = new_fecha_registro
            )

            new_paciente.save()
            return render(request, 'pacientes/add.html', {
                'form': PacienteForm(),
                'success': True
            })
    else:
        form = PacienteForm()
    return render(request, 'pacientes/add.html', {
        'form': PacienteForm
    })

def edit(request, id):
    if request.method == 'POST':
        paciente = Paciente.objects.get(pk=id)
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return render(request, 'pacientes/edit.html', {
                'form': form,
                'success': True
            })
    else:
        paciente = Paciente.objects.get(pk=id)
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/edit.html', {
        'form': form,
    })

def delete(request, id):
    if request.method == 'POST':
        paciente = Paciente.objects.get(pk=id)
        paciente.delete()
    return HttpResponseRedirect(reverse('index'))