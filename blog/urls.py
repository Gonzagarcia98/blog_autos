"""
URL configuration for blog_autos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.urls import path
from .views import (
    PageListView, 
    PageDetailView, 
    PageCreateView, 
    PageUpdateView, 
    PageDeleteView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('auto/nuevo/', views.auto_nuevo, name='auto_nuevo'),
    path('auto/editar/<int:pk>/', views.auto_editar, name='auto_editar'),
    path('auto/<int:pk>/', views.auto_detalle, name='auto_detalle'),
    path('auto/like/<int:auto_id>/', views.toggle_like, name='toggle_like'),
    path('auto/<int:pk>/eliminar/', views.auto_eliminar, name='auto_eliminar'),
    path('categoria/nueva/', views.categoria_nueva, name='categoria_nueva'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('pages/', PageListView.as_view(), name='page_list'),
    path('pages/<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('pages/new/', PageCreateView.as_view(), name='page_create'),
    path('pages/<int:pk>/edit/', PageUpdateView.as_view(), name='page_update'),
    path('pages/<int:pk>/delete/', PageDeleteView.as_view(), name='page_delete'),
]