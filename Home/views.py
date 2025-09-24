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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("inicio")  # Después del login → va al menú de productos
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def inicio(request):
    return render(request, "inicio.html")
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto  # Asegúrate de importar tu modelo
from .forms import ProductoForm  # Y tu formulario

# ... tus otras vistas existentes ...

@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'agregar_producto.html', {'form': form, 'editar': True})

@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'confirmar_eliminar.html', {'producto': producto})