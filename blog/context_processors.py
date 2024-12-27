from .models import Auto
from django.contrib.auth.models import User

def filtros_context(request):
    return {
        'autores': User.objects.filter(autos__isnull=False).distinct(),
        'marcas': Auto.objects.values_list('marca', flat=True).distinct()
    }