from django.core.exceptions import ValidationError

def validate_password_length(value):
    if len(value) < 8:
        raise ValidationError('La contraseña debe tener al menos 8 caracteres.')    