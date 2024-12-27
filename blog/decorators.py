from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def superuser_required(view_func):
    """Decorador que verifica si el usuario es superusuario."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "Solo los administradores pueden acceder a esta página.")
            return redirect('home')
    return _wrapped_view