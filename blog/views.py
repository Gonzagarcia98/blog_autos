from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.db.models import Q
from .models import Auto, Categoria
from .forms import AutoForm, CategoriaForm
from .models import SobreMi
from .forms import SobreMiForm
import random
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Page
from .mixins import SuperuserRequiredMixin
from .decorators import superuser_required
from django.contrib.auth.models import User

def es_superusuario(user):
    return user.is_superuser

def home(request):
    # Iniciar el queryset con todos los autos
    autos = Auto.objects.all()
    context = {'autos': autos}
    
    # Solo procesar filtros si el usuario está autenticado
    if request.user.is_authenticated:
        # Obtener todas las marcas y modelos únicos
        marcas = Auto.objects.values_list('marca', flat=True).distinct()
        modelos = Auto.objects.values_list('modelo', flat=True).distinct()
        
        # Aplicar filtros si existen
        marca = request.GET.get('marca')
        modelo = request.GET.get('modelo')
        
        if marca:
            autos = autos.filter(marca=marca)
        if modelo:
            autos = autos.filter(modelo=modelo)
            
        # Agregar datos de filtros al contexto
        context.update({
            'marcas': marcas,
            'modelos': modelos,
            'marca_seleccionada': marca,
            'modelo_seleccionado': modelo
        })
    
    return render(request, 'blog/home.html', context)

@login_required
@superuser_required
def auto_nuevo(request):
    if request.method == "POST":
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            auto = form.save(commit=False)
            auto.usuario = request.user
            auto.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = AutoForm()
    return render(request, 'blog/auto_form.html', {'form': form})

@login_required
def auto_editar(request, pk):
    if not request.user.is_superuser:
        return redirect('home')
    auto = get_object_or_404(Auto, pk=pk)
    if request.method == "POST":
        form = AutoForm(request.POST, request.FILES, instance=auto)
        if form.is_valid():
            auto = form.save()
            return redirect('home')
    else:
        form = AutoForm(instance=auto)
    return render(request, 'blog/auto_form.html', {'form': form, 'editing': True})

def auto_detalle(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    return render(request, 'blog/auto_detalle.html', {'auto': auto})

@login_required
def toggle_like(request, auto_id):
    auto = get_object_or_404(Auto, id=auto_id)
    if request.user in auto.likes.all():
        auto.likes.remove(request.user)
        liked = False
    else:
        auto.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked})

@login_required
def categoria_nueva(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'blog/categoria_form.html', {'form': form})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'blog/lista_categorias.html', {'categorias': categorias})

@user_passes_test(es_superusuario)
def auto_eliminar(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            # Primera confirmación pasada, mostrar cálculo
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            request.session['calculo'] = {'num1': num1, 'num2': num2, 'resultado': num1 + num2}
            return render(request, 'blog/auto_confirmar_calculo.html', {
                'auto': auto,
                'num1': num1,
                'num2': num2,
                'next': request.GET.get('next', 'home')
            })
        elif 'confirm_calculo' in request.POST:
            # Verificar cálculo
            calculo = request.session.get('calculo', {})
            respuesta = request.POST.get('respuesta')
            if respuesta and int(respuesta) == calculo.get('resultado'):
                # Guardar información para mensaje de éxito
                marca = auto.marca
                modelo = auto.modelo
                año = auto.año
                next_page = request.POST.get('next', 'home')
                # Eliminar la imagen si existe
                if auto.imagen:
                    auto.imagen.delete()
                auto.delete()
                return render(request, 'blog/auto_eliminado.html', {
                    'marca': marca,
                    'modelo': modelo,
                    'año': año,
                    'next': next_page
                })
    
    return render(request, 'blog/auto_confirmar_eliminar.html', {
        'auto': auto,
        'next': request.GET.get('next', 'home')
    })
def sobre_mi(request):
    info = SobreMi.objects.first()
    if request.method == "POST" and request.user.is_superuser:
        form = SobreMiForm(request.POST, request.FILES, instance=info)
        if form.is_valid():
            form.save()
            return redirect('sobre_mi')
    else:
        form = SobreMiForm(instance=info) if info else SobreMiForm()
    
    return render(request, 'blog/sobre_mi.html', {
        'info': info,
        'form': form if request.user.is_superuser else None
    })

class PageListView(ListView):
    model = Page
    template_name = 'blog/pages/list.html'
    context_object_name = 'pages'
    ordering = ['-fecha_creacion']

class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/pages/detail.html'
    context_object_name = 'page'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    template_name = 'blog/pages/form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    success_url = reverse_lazy('page_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Page
    template_name = 'blog/pages/form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    success_url = reverse_lazy('page_list')

    def test_func(self):
        page = self.get_object()
        return self.request.user == page.autor or self.request.user.is_superuser

class PageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Page
    template_name = 'blog/pages/confirm_delete.html'
    success_url = reverse_lazy('page_list')

    def test_func(self):
        page = self.get_object()
        return self.request.user == page.autor or self.request.user.is_superuser

class AutoCreateView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = Auto
    template_name = 'blog/auto_form.html'
    fields = ['marca', 'modelo', 'año', 'descripcion', 'imagen', 'categorias']
    success_url = reverse_lazy('home')