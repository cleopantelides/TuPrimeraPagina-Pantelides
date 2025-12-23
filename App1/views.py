from django.shortcuts import render
from .forms import AutorForm, CategoriaForm, PostForm
from .models import Post

def inicio(request):
    return render(request, "App1/inicio.html")

def crear_autor(request):
    form = AutorForm()
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "App1/crear_autor.html", {"form": form})

def crear_categoria(request):
    form = CategoriaForm()
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "App1/crear_categoria.html", {"form": form})

def crear_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "App1/crear_post.html", {"form": form})

def buscar_post(request):
    resultados = []
    if request.GET.get("titulo"):
        resultados = Post.objects.filter(titulo__icontains=request.GET["titulo"])
    return render(request, "App1/buscar_post.html", {"resultados": resultados})
