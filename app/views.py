from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Lugar
from .forms import LugarForm
import logging
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
##from django.shortcuts import render, redirect
#from django.shortcuts import get_object_or_404, redirect, render


def login_view(request):
    """Vista para el inicio de sesión"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'app/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'app/login.html')

@login_required
def home_view(request):
    """Vista para la página principal"""
    return render(request, 'app/home.html')

@login_required
def containers_view(request):
    """Vista para mostrar los eventos"""
    return render(request, 'app/eventos.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige al login después de cerrar sesión

def register_view(request):
    user_registered = False  # Variable para controlar si el usuario fue registrado

    if request.method == 'POST':
        try:
            form = CustomUserCreationForm(request.POST)
            
            if form.is_valid():
                form.save()
                user_registered = True  # El usuario fue registrado
                messages.success(request, '¡Usuario registrado exitosamente!')
                return redirect('login')  # Redirigir al inicio de sesión después del registro
            
            else:
                messages.error(request, 'Corrige los errores en el formulario.')
        
        # Manejo de duplicidad de usuario
        except IntegrityError as e:
            messages.error(request, 'El usuario ya existe. Intente con otro nombre de usuario o correo.')
        
        # Manejo de errores generales
        except Exception as e:
            messages.error(request, f'Ocurrió un error inesperado: {e}')
    
    else:
        form = CustomUserCreationForm()

    return render(request, 'app/register.html', {'form': form, 'user_registered': user_registered})

@login_required
def user_list_view(request):
    User = get_user_model()
    users = User.objects.all()  # Obtén todos los usuarios
    return render(request, 'app/usuarios/user_list.html', {'users': users})

def editar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        usuario.username = request.POST['username']
        usuario.email = request.POST['email']
        usuario.save()
        messages.success(request, 'Usuario editado correctamente.')
        return redirect('user_list')
    return render(request, 'app/editar_usuario.html', {'usuario': usuario})



def eliminar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente.')
        return redirect('user_list')
    return render(request, 'app/confirmar_eliminar_usuario.html', {'usuario': usuario})



def agregar_lugar_usuario(request):
    if request.method == 'POST':
        form = LugarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡El lugar ha sido agregado exitosamente!")
            return redirect('lista_lugares')
    else:
        form = LugarForm()
    return render(request, 'lugares/agregar_lugar.html', {'form': form})


def lista_lugares(request):
    lugares = Lugar.objects.all()
    return render(request, 'lugares/lista_lugares.html', {'lugares': lugares})




def admin_lista_lugares(request):
    lugares = Lugar.objects.all()
    return render(request, 'admin/lugares/admin_lista_lugares.html', {'lugares': lugares})

def agregar_lugar_admin(request):
    if request.method == 'POST':
        form = LugarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_lista_lugares')
    else:
        form = LugarForm()
    return render(request, 'admin/lugares/agregar_lugar_admin.html', {'form': form})

def editar_lugar(request, lugar_id):
    lugar = get_object_or_404(Lugar, id=lugar_id)
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        direccion = request.POST.get('direccion')
        url_mapa = request.POST.get('url_mapa')

        # Actualizar valores
        lugar.nombre = nombre
        lugar.descripcion = descripcion
        lugar.direccion = direccion
        lugar.url_mapa = url_mapa
        lugar.save()

        return redirect('admin_lista_lugares')
    
    return render(request, 'admin/lugares/editar_lugar.html', {'lugar': lugar})

def agregar_lugar_admin(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        direccion = request.POST['direccion']
        latitud = request.POST.get('latitud')
        longitud = request.POST.get('longitud')
        url_mapa = request.POST.get('url_mapa')
        
        Lugar.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            direccion=direccion,
            latitud=latitud,
            longitud=longitud,
            url_mapa=url_mapa
        )
        return redirect('admi_lugar')
    return render(request, 'app/agregar_lugar_admin.html')

def eliminar_lugar(request, lugar_id):
    lugar = get_object_or_404(Lugar, id=lugar_id)
    
    if request.method == 'POST':
        lugar.delete()
        return redirect('admin_lista_lugares')
    
    return render(request, 'admin/lugares/eliminar_lugar.html', {'lugar': lugar})

def nueva_pagina(request):
    return render(request, 'app/inicio.html')  # Nombre del template


logger = logging.getLogger(__name__)

def eventos(request):
    query = request.GET.get('q', '')
    if query:
        lista_lugares = Lugar.objects.filter(nombre__icontains=query)
    else:
        lista_lugares = Lugar.objects.all()

    logger.debug(f"Lista de lugares: {lista_lugares}")

    return render(request, 'eventos.html', {'lista_lugares': lista_lugares, 'query': query})

def contact(request):
    if request.method == 'POST':
        try:
            # Captura los datos del formulario
            name = request.POST.get('name')
            address = request.POST.get('address')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            
            # Validación de campos vacíos
            if not name or not email or not message:
                raise ValidationError("Los campos Nombre, Email y Mensaje son obligatorios.")
            
            # Validación de email
            validate_email(email)
            
            # Simulación de procesamiento exitoso
            print(f"Contacto recibido de {name} ({email}): {message}")
            
            messages.success(request, '¡Gracias por contactarnos! Te responderemos pronto.')
            return render(request, 'app/contact.html', {'name': name})
        
        except ValidationError as e:
            messages.error(request, f'Error de validación: {e}')
        except Exception as e:
            messages.error(request, f'Ocurrió un error inesperado: {e}')
    
    return render(request, 'app/contact.html')

def admin_lista_lugares(request):
    lugares = Lugar.objects.all()
    return render(request, 'admin/lugares/admin_lista_lugares.html', {'lugares': lugares})

