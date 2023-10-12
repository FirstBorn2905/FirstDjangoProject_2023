import os
from random import randrange
from main.wsgi import *
from main import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Personal, Solicitud, ReporteVentas
from .forms import PersonalForm, SolicitudForm, ReporteForm
from django.contrib.auth.decorators import login_required
#PDF extra
from django.template.loader import get_template #Acceso a templates
from django.http import HttpResponse
# --------------------------------------
from weasyprint import HTML, CSS
#Grafico de ventas
from django.http.response import JsonResponse

# PDF Generator
def showSolicity(request):
    solicitud = Solicitud.objects.all()
    return render (request, 'archivoPDf.html',{'solicitud': solicitud})

def downloadSolicity(request):
    solicitud = Solicitud.objects.all() #Se crea la instancia para llamar a las variables del modelo
    
    # Path del html a convertir
    template_path = 'archivoPDF.html' 
    
    # Diccionario donde se almacena la instancia de la clase/modelo
    context = { 
        'solicitud': solicitud,
        'user': request.user #Para poder imprimir el nombre del user
    }
    
    #-------WEASYPRINT Version---------
    template = get_template(template_path)
    html_template = template.render(context)
    css_url = os.path.join(settings.BASE_DIR, 'static/bootstrap/css/bootstrap.min.css') #URL DEL CSS/BOOTSTRAP URGENTE!!!!!
    pdf = HTML(string=html_template).write_pdf(stylesheets=[CSS(css_url)])
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ReportePDF.pdf"'
    return response


# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #Validación
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/') #direccionamiento a home
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    
def signin(request):
    # if request.user.is_authenticated:
    #     return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main') #direccionamiento a home
        else:
            error = 'Usuario o contraseña incorrectas'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'error': error})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html',{'form': form})

def signout(request):
    logout(request)
    return redirect('/')

@login_required 
def main(request):
    personal1 = Personal.objects.count()
    solicitud1 = Solicitud.objects.count()
    reporte1 = ReporteVentas.objects.count()
    
    personal2 = Personal.objects.all()
    solicitud2 = Solicitud.objects.all()
    reporte2 = ReporteVentas.objects.all()
    context = {
        'personalCant': personal1,
        'solicitudCant': solicitud1,
        'reporteCant': reporte1,
        
        'personal': personal2,
        'solicitud': solicitud2,
        'reporte': reporte2,
    }
    return render(request, 'main.html', context)

# --------- PERSONAL ----------------------
@login_required 
def personal(request):
    personal = Personal.objects.all()
    return render(request, 'personal.html',{'personal': personal})

@login_required 
def crearPersonal(request):
    formulario = PersonalForm(request.POST or None, request.FILES or None)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('personal')
    return render(request, 'crearPersonal.html', {'form': formulario})

@login_required 
def editarPersonal(request, id):
    personal = Personal.objects.get(id = id)
    formulario = PersonalForm(request.POST or None, request.FILES or None, instance=personal)
    if formulario.is_valid():
        formulario.save()
        return redirect('personal')
    return render(request, 'editarPersonal.html', {'form': formulario})

@login_required 
def eliminarPersonal(request, id):
    personal = Personal.objects.get(id = id)
    personal.delete()
    return redirect ('personal')

# --------- VENTAS ----------------------
@login_required 
def ventas(request):
    return render(request, 'ventas.html')

@login_required 
def generateReports(request):
    reporte = ReporteVentas.objects.all()
    if request.method == 'POST':
        # Para validar el formulario de reportes
        form = ReporteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reportes')
    else:
        form = ReporteForm()
        
    context = {
        'reporte': reporte,
        'form': form
    }
    return render(request, 'reportes.html', context)

@login_required
def eliminarReporte(request, id):
    reporte = ReporteVentas.objects.get(id = id)
    reporte.delete()
    return redirect('reportes')

#Graffic generator
@login_required
def renderGraffic(request):
    reporte = ReporteVentas.objects.all()
    
    if request.method == 'GET':
        form = ReporteForm()
        
    context = {
        'reporte': reporte,
        'form': form
    }
    return render (request, 'graficos.html', context)

# --------- ALMACEN ----------------------
@login_required 
def almacen(request):
    solicitud = Solicitud.objects.all()
    return render(request, 'almacen.html',{'solicitud': solicitud})

@login_required 
def crearSolicitud(request):
    formulario = SolicitudForm(request.POST or None, request.FILES or None)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('almacen')
    return render(request, 'crearSolicitud.html', {'form': formulario})

@login_required 
def eliminarSolicitud(request, id):
    solicitud = Solicitud.objects.get(id = id)
    solicitud.delete()
    return redirect ('almacen')

