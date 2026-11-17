# core/urls.py
from django.contrib import admin
from django.urls import path, include
from core.views import InicioView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ruta principal con nombre global 'inicio'
    path('', InicioView.as_view(), name='inicio'),
    
    # Inclusión de aplicaciones (los namespaces se toman de app_name en cada urls.py)
    path('productos/', include('productos.urls')),
    path('proveedores/', include('proveedores.urls')),
    path('clientes/', include('clientes.urls')),
    path('ventas/', include('ventas.urls')),
    path('reportes/', include('reportes.urls')),
    path('configuracion/', include('configuracion.urls')),
    
    # Autenticación
    path('accounts/', include('allauth.urls')),
]




   