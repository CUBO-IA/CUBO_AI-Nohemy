from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar-carrito/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
]
