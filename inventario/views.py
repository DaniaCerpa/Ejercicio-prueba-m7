from django.shortcuts import render
from .models import Producto, Categoria
 
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Min, Max
 
 
# Create your views here.
 
def listado_productos_view(request):
   
    nombre = request.GET.get('nombre')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    fecha_vencimiento_max = request.GET.get('fecha_vencimiento_max')
    fecha_vencimiento_min = request.GET.get('fecha_vencimiento_min')
   
    if not nombre:
        nombre = ""
   
    contexto = {}
    productos = Producto.objects.all().order_by('-fecha_vencimiento')
   
    if nombre:
        productos = productos.filter(Q(nombre__icontains=nombre) | Q(descripcion__icontains=nombre))
       
    if precio_min:
        productos = productos.filter(precio__gte=precio_min)
       
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)
        
    if fecha_vencimiento_min:
        productos = productos.filter(fecha_vencimiento__gte=fecha_vencimiento_min)
       
    if fecha_vencimiento_max:
        productos = productos.filter(fecha_vencimiento__lte=fecha_vencimiento_max)
       
    #Se utiliza min y max (built-in function de python para evitar realizar mas consultas a la BD)   
    limite_min= min((p.fecha_vencimiento for p in productos if p.fecha_vencimiento), default=None) 
    limite_max= max((p.fecha_vencimiento for p in productos if p.fecha_vencimiento), default=None)       
        
    contexto["productos"] = productos
    contexto["categorias"] = Categoria.objects.all().order_by("nombre")
    contexto["nombre"] = nombre
    contexto["precio_min"] = precio_min
    contexto["precio_max"] = precio_max
    contexto["fecha_vencimiento_min"] = fecha_vencimiento_min
    contexto["fecha_vencimiento_max"] = fecha_vencimiento_max
    contexto["limite_min"] = limite_min
    contexto["limite_max"] = limite_max
   
    return render(request, 'listado_productos.html', contexto)
 