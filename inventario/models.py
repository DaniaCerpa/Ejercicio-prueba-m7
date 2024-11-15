from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    precio = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'productos'


