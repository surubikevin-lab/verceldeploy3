from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm
from .models import Producto

# Vista de login
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("inicio")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "login.html")

# Vista de logout
def user_logout(request):
    logout(request)
    return redirect("login")

# VISTAS PROTEGIDAS CON LOGIN REQUIRED
@login_required
def inicio(request):
    return render(request, 'inicio.html')

@login_required
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

@login_required
def lista_productos(request):
    productos = Producto.objects.all().order_by('-created')
    return render(request, 'lista_productos.html', {'productos': productos})

@login_required
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

@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'confirmar_eliminar.html', {'producto': producto})