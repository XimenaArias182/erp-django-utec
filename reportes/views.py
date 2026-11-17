# reportes/views.py
from django.views.generic import TemplateView


class ReporteListView(TemplateView):
    """Vista principal para el módulo de reportes."""

    template_name = 'reportes/lista.html'