from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.nombre

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


    def __str__(self):
        return self.nombre
    
    def clean(self):
        if self.fecha_vencimiento and self.fecha_vencimiento < timezone.now().date():
            raise ValidationError("La fecha de vencimiento debe ser igual o posterior a la fecha actual.")
 
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
    class Meta:
        managed = False
        db_table = 'productos'



    