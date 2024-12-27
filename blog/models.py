from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField 

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre

class Auto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='autos')
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='autos/', null=True, blank=True)
    categorias = models.ManyToManyField(Categoria, related_name='autos_categoria', blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='autos_liked', blank=True)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"

class Reseña(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='reseñas')
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
class SobreMi(models.Model):
    texto = models.TextField()
    imagen = models.ImageField(upload_to='about/', null=True, blank=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sobre Mí - Última actualización: {self.ultima_actualizacion}"

    class Meta:
        verbose_name = "Sobre Mí"
        verbose_name_plural = "Sobre Mí"

class Page(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    contenido = RichTextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='pages/', null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha_creacion']