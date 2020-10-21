from django.shortcuts import render_to_response, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import (authenticate, login, logout)
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
import hashlib, datetime, random
from django.utils import timezone
from django.conf import settings
from User.models import auth_user
from django.http import JsonResponse
from Cliente.views import CrearCliente
import json
from Cliente.models import Cliente
from django.contrib.auth.decorators import login_required


def SignUp(request):
    data = json.loads(request.body)
    user = auth_user.objects.create_user(email=data['email'], username=data['email'], password='1234', nombres=data['nombres'], apellidos=['apellidos'])
    CrearCliente(user.id, data['empresa'], data['ruc'], data['direccion'])
    exito = {'status': 'usuario creado'}
    return JsonResponse(exito)


def register_confirm(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('/')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(auth_user, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now().date():
        return render_to_response('/')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile
    user.is_active = True
    user.save()
    return HttpResponseRedirect("/login")


def Login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:  # aqui revisa si los datos ingresados son permitidos en el campo
            mail = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(email=mail.lower(), password=clave)
            if acceso is not None:
                login(request, acceso)
                ctx = {'mail': mail, }
                return HttpResponseRedirect("/files/%s" % acceso.cliente.cod_cliente)
            else:
                formulario = AuthenticationForm()
                mensaje = "Datos Incorrectos, verifica tu usuario y clave"
                ctx = {'formulario':formulario, 'mensaje': mensaje}
                return render(request, 'user/login.html', context=ctx)
        else:
            formulario = AuthenticationForm()
            mensaje = "Valores Incorrectos"
            ctx = {'formulario':formulario,'mensaje': mensaje}
            return render(request, 'user/login.html', context=ctx)
    else:
        formulario = AuthenticationForm()
    ctx = {'formulario':formulario,}
    return render(request, 'user/login.html', context=ctx)

@login_required(login_url='/login/')
def Inicio(request):
    cod_cliente = Cliente.objects.get(usuario=request.user).cod_cliente
    return HttpResponseRedirect("/files/%s" % cod_cliente)


@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect("/")