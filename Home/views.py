from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm
from .models import Producto

# Pantalla inicial
def inicio(request):
    return render(request, 'inicio.html')

# Agregar nuevo producto
def agregar_producto(request):
    mensaje = None
    form = ProductoForm()

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "✅ Registrado Correctamente"
            form = ProductoForm()  # limpiar formulario

    return render(request, 'agregar_producto.html', {'form': form, 'mensaje': mensaje})

# Lista de productos
def lista_productos(request):
    productos = Producto.objects.all().order_by('-created')
    return render(request, 'lista_productos.html', {'productos': productos})

# Editar producto
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    mensaje = None
    form = ProductoForm(instance=producto)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            mensaje = "✅ Producto actualizado correctamente"

    return render(request, 'agregar_producto.html', {'form': form, 'mensaje': mensaje, 'editar': True})

# Eliminar producto
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('lista_productos')
