from django.contrib import admin
from .models import Categoria, Producto
 
# Register your models here.
 
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
   
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'fecha_vencimiento')
    search_fields = ('nombre', 'categoria',)
    list_filter = ('categoria',)
   
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)