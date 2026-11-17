# core/mixins.py
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied


class ERPAuthPermissionMixin(LoginRequiredMixin, PermissionRequiredMixin):
    """Redirige a login (302) si es anonimo y valida permisos RBAC (403) si tiene rol."""

    raise_exception = True

    def has_permission(self):
        user = self.request.user
        if not user.is_authenticated:
            return False
        if user.is_superuser or user.groups.exists() or user.user_permissions.exists():
            return super().has_permission()
        return True

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect_to_login(
                self.request.get_full_path(),
                self.get_login_url(),
                self.get_redirect_field_name(),
            )
        raise PermissionDenied(self.get_permission_denied_message())
