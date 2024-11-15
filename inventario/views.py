from django.shortcuts import render
from .models import Producto, Categoria
 
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Min, Max
 
 
# Create your views here.
 
def listado_productos_view(request):
   
    nombre = request.GET.get('nombre')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
   
    if not nombre:
        nombre = ""
   
    contexto = {}
    productos = Producto.objects.all()
   
    if nombre:
        productos = productos.filter(Q(nombre__icontains=nombre) | Q(descripcion__icontains=nombre))
       
    if precio_min:
        productos = productos.filter(precio__gte=precio_min)
       
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)
       
       
    contexto["productos"] = productos
    contexto["categorias"] = Categoria.objects.all()
    contexto["nombre"] = nombre
    contexto["precio_min"] = precio_min
    contexto["precio_max"] = precio_max
   
    return render(request, 'listado_productos.html', contexto)
 