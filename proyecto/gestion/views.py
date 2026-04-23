from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Libro
from .forms import AutorForm, LibroForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# CRUD Autores (funciones)
def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'gestion/autor_list.html', {'autores': autores})


def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'gestion/autor_create.html', {'form': form})


def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'gestion/autor_update.html', {'form': form})


def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'gestion/autor_delete.html', {'autor': autor})


# CRUD Libros (funciones)
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'gestion/libro_list.html', {'libros': libros})


def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'gestion/libro_create.html', {'form': form})


def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'gestion/libro_update.html', {'form': form})


def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'gestion/libro_delete.html', {'libro': libro})


# Vistas genéricas
class AutorListView(ListView):
    model = Autor
    template_name = 'gestion/autor_list.html'
    context_object_name = 'autores'


class LibroListView(ListView):
    model = Libro
    template_name = 'gestion/libro_list.html'
    context_object_name = 'libros'


class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_create.html'
    success_url = reverse_lazy('lista_autores')


class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/libro_create.html'
    success_url = reverse_lazy('lista_libros')


class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_update.html'
    success_url = reverse_lazy('lista_autores')


class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/libro_update.html'
    success_url = reverse_lazy('lista_libros')


class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'gestion/autor_delete.html'
    success_url = reverse_lazy('lista_autores')


class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'gestion/libro_delete.html'
    success_url = reverse_lazy('lista_libros')

def inicio(request):
    return render(request, 'gestion/inicio.html')