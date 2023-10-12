from django.urls import path
from . import views
# from .views import GeneratePDF

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name='home'),
    path("signin/", views.signin, name='signin'),
    path("signout/", views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('main/', views.main, name='main'),
    # Area de Personal
    path('personal/', views.personal, name='personal'),
    path('personal/crear/', views.crearPersonal, name='crearPersonal'),
    path('eliminarPersonal/<int:id>', views.eliminarPersonal, name='eliminarPersonal'),
    path('personal/editar/<int:id>', views.editarPersonal, name='editarPersonal'),
    # Area de Ventas
    path('ventas/', views.ventas, name='ventas'),
    path('ventas/grafico', views.renderGraffic, name='grafico'),
    path('ventas/reportes', views.generateReports, name='reportes'),
    path('eliminarReporte/<int:id>', views.eliminarReporte, name='eliminarReporte'),
    # path('ventas/chart/', views.get_chart, name='getChart'),
    # Area de Almacen
    path('almacen/', views.almacen, name='almacen'),
    #------------PDF GENERATOR----------------------------------------------
    # path('createPDF/', views.showSolicity, name='downloadPDF'),
    path('createPDF/', views.downloadSolicity, name='downloadPDF'),
    #-------------------------------------------------------------------------
    path('almacen/solicitud', views.crearSolicitud, name='crearSolicitud'),
    path('eliminarSolicitud/<int:id>', views.eliminarSolicitud, name='eliminarSolicitud'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
