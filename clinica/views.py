from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from .models import Paciente, Medico
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import HistorialMedicoForm

# Registro


def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_pacientes')  # Redirige después del registro
    else:
        form = UserCreationForm()
    return render(request, 'clinica/registro.html', {'form': form})

# Login


def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_pacientes')
    else:
        form = AuthenticationForm()
    return render(request, 'clinica/login.html', {'form': form})

# Logout


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion')

# Lista de pacientes


@login_required
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'clinica/lista_pacientes.html', {'pacientes': pacientes})

# Editar historial médico


@login_required
def editar_historial(request, paciente_id=None):
    """
    Si el usuario es paciente, edita su propio historial.
    Si es médico, edita el historial de un paciente específico.
    """
    if hasattr(request.user, 'paciente'):
        paciente = get_object_or_404(Paciente, usuario=request.user)
    elif hasattr(request.user, 'medico') and paciente_id:
        paciente = get_object_or_404(Paciente, id=paciente_id)
    else:
        return redirect('lista_pacientes')

    if request.method == "POST":
        form = HistorialMedicoForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = HistorialMedicoForm(instance=paciente)

    return render(request, 'clinica/editar_historial.html', {'form': form, 'paciente': paciente})

# Búsqueda de pacientes


@login_required
def buscar_pacientes(request):
    query = request.GET.get('q', '')
    pacientes = Paciente.objects.filter(
        nombre__icontains=query) if query else Paciente.objects.none()
    return render(request, 'clinica/buscar_pacientes.html', {'pacientes': pacientes, 'query': query})
