# clientes/views.py
"""Vistas de la app clientes con control de acceso RBAC."""
from django.contrib import messages
from core.mixins import ERPAuthPermissionMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from .forms import ClienteForm
from .models import Cliente


class ClienteListView(ListView):
    """Lista paginada de clientes activos."""

    model = Cliente
    template_name = 'clientes/lista.html'
    context_object_name = 'clientes'
    paginate_by = 20

    def get_queryset(self):
        return Cliente.objects.filter(activo=True).order_by('nombre')


class ClienteDetailView(DetailView):
    """Detalle de un cliente."""

    model = Cliente
    template_name = 'clientes/detalle.html'
    context_object_name = 'cliente'


class ClienteCreateView(ERPAuthPermissionMixin, CreateView):
    """Formulario para crear un nuevo cliente."""

    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/crear.html'
    permission_required = 'clientes.add_cliente'
    raise_exception = True
    success_url = reverse_lazy('clientes:lista')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            f'Cliente "{self.object.nombre}" creado exitosamente.'
        )
        return response


class ClienteUpdateView(ERPAuthPermissionMixin, UpdateView):
    """Formulario para editar un cliente."""

    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/editar.html'
    permission_required = 'clientes.change_cliente'
    raise_exception = True
    success_url = reverse_lazy('clientes:lista')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            f'Cliente "{self.object.nombre}" actualizado.'
        )
        return response


class ClienteDeleteView(ERPAuthPermissionMixin, DeleteView):
    """Confirmación y borrado de un cliente."""

    model = Cliente
    template_name = 'clientes/eliminar.html'
    permission_required = 'clientes.delete_cliente'
    raise_exception = True
    success_url = reverse_lazy('clientes:lista')

    def form_valid(self, form):
        nombre = self.object.nombre
        response = super().form_valid(form)
        messages.success(self.request, f'Cliente "{nombre}" eliminado.')
        return response