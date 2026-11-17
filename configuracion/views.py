# configuracion/views.py
from django.views.generic import TemplateView


class ConfiguracionDetailView(TemplateView):
    """Vista principal de ajustes del ERP."""

    template_name = 'configuracion/detalle.html'