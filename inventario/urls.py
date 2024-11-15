from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.listado_productos_view, name= 'listado_productos'),
]

