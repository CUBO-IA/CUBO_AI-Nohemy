

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto


def inicio(request):
    return render(request, 'inicio.html')


def productos(request):
    productos = Producto.objects.all()

    return render(
        request,
        'productos.html',
        {'productos': productos}
    )


def agregar_carrito(request, producto_id):

    producto = get_object_or_404(Producto, id=producto_id)

    carrito = request.session.get('carrito', {})

    producto_id = str(producto_id)

    if producto_id in carrito:
        carrito[producto_id] += 1
    else:
        carrito[producto_id] = 1

    request.session['carrito'] = carrito

    return redirect('productos')


def carrito(request):

    carrito = request.session.get('carrito', {})

    productos = []
    total = 0

    for producto_id, cantidad in carrito.items():

        producto = get_object_or_404(
            Producto,
            id=producto_id
        )

        subtotal = producto.precio * cantidad

        productos.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

        total += subtotal

    return render(
        request,
        'carrito.html',
        {
            'productos': productos,
            'total': total
        }
    )
