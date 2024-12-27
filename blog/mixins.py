from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib import messages

class SuperuserRequiredMixin(UserPassesTestMixin):
    """Mixin que verifica si el usuario es superusuario."""
    
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "Solo los administradores pueden acceder a esta página.")
        return redirect('home')