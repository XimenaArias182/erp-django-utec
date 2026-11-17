# core/views.py
from django.views.generic import TemplateView
from django.urls import reverse_lazy, NoReverseMatch, reverse


class InicioView(TemplateView):
    """Vista principal que renderiza el panel con los 6 módulos del ERP."""

    template_name = 'bienvenida.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modulos'] = [
            {
                'nombre': 'Productos',
                'icono': '📦',
                'descripcion': 'Gestión de catálogo, categorías y stock.',
                'url': reverse_lazy('productos:lista'),
            },
            {
                'nombre': 'Proveedores',
                'icono': '🏭',
                'descripcion': 'Directorio y gestión de proveedores.',
                'url': reverse_lazy('proveedores:lista'),
            },
            {
                'nombre': 'Clientes',
                'icono': '👥',
                'descripcion': 'Gestión de clientes y contactos.',
                'url': reverse_lazy('clientes:lista'),
            },
            {
                'nombre': 'Ventas',
                'icono': '🛒',
                'descripcion': 'Registro de ventas y pedidos.',
                'url': reverse_lazy('ventas:lista'),
            },
            {
                'nombre': 'Reportes',
                'icono': '📊',
                'descripcion': 'Informes y estadísticas del sistema.',
                'url': self._obtener_url('reportes:lista'),
            },
            {
                'nombre': 'Configuración',
                'icono': '⚙️',
                'descripcion': 'Ajustes generales del ERP.',
                'url': self._obtener_url('configuracion:detalle'),
            },
        ]
        return context

    def _obtener_url(self, nombre_ruta):
        try:
            return reverse(nombre_ruta)
        except NoReverseMatch:
            return '#'


bienvenida = InicioView.as_view()