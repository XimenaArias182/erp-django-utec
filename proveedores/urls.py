# proovedores/urls.py
"""URLs de la app proovedores — W01 (mínimo funcional)."""
from django.urls import path
from django.http import HttpResponse

app_name = 'proovedores'


def bienvenida_proovedores(request):
    """Vista temporal de bienvenida para la app proovedores."""
    return HttpResponse(
        "<h2>📦 Módulo proovedores</h2>"
        "<p>En construcción — Espiral 2 (W04)</p>",
        content_type='text/html; charset=utf-8'
    )


urlpatterns = [
    path('', bienvenida_proovedores, name='inicio'),
]
