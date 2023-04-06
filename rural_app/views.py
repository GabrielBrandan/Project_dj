from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.models import User
from .forms import ColectivosForms
from .models import Colectivos
from django.db.models import Q



def inicio(request):
    return render(request, 'inicio.html')


def registro_de_usuarios(request):
    if request.method == 'GET':
        return render(request, 'registro_de_usuarios.html', {"form": UserCreationForm})

    else:
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if len(password1) < 8:
            return render(request, 'registro_de_usuarios.html', {"form": UserCreationForm, "error": "La contraseña debe tener al menos 8 caracteres."})
    
        elif password1 == password2:
            try:
                user = User.objects.create_user(request.POST["username"], password=password1)
                user.save()
                login(request, user)
                return redirect('inicio')
            except IntegrityError:
                return render(request, 'registro_de_usuarios.html', {"form": UserCreationForm, "error": "El nombre de usuario ya existe."})

        return render(request, 'registro_de_usuarios.html', {"form": UserCreationForm, "error": "Las contraseñas no coinciden."})


def inicio_de_seccion(request):
    if request.method == 'GET':
        return render(request, 'inicio_de_seccion.html', {"form": AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'inicio_de_seccion.html', {"form": AuthenticationForm, "error": "Nombre de usuario o contraseña incorrecta."})
        login(request, user)
        return redirect('inicio')


@login_required
def cierre_de_seccion(request):
    logout(request)
    return redirect('inicio')


@login_required
def registro_de_colectivos(request):
    if request.method == 'POST':
        colectivosform = ColectivosForms(request.POST)
        if colectivosform.is_valid():
            colectivos = colectivosform.save(commit=False)
            colectivos.user = request.user
            colectivos.save()
            return redirect('colectivos')

    return render(request, 'registro_de_colectivos.html', {
        'colectivosform': ColectivosForms,
    })
    

@login_required
def colectivos(request):
    colectivos = Colectivos.objects.filter(user=request.user)
    return render(request, 'colectivos.html', {'colectivos': colectivos,})



@login_required
def eliminar_colectivo(request, colectivo_id):
    eliminar_colectivo = get_object_or_404(Colectivos, pk=colectivo_id, user=request.user)
    if request.method == 'POST':
        eliminar_colectivo.delete()
        return redirect('colectivos')


def buscador_de_colectivos(request):
    busqueda = request.GET.get('buscar')
    colectivos = Colectivos.objects.all()
    if busqueda:
        colectivos = Colectivos.objects.filter(
            Q(origen__icontains = busqueda) |
            Q(destino__icontains = busqueda) |
            Q(hora_salida__icontains = busqueda) |
            Q(dias_de_circulacion__icontains = busqueda) |
            Q(compania__icontains = busqueda) |
            Q(precio__icontains = busqueda) 
            ).distinct() 

    return render(request, 'buscador_de_colectivos.html', {'colectivos':colectivos})