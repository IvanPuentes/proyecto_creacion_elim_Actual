from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,DescripLib,Manga,Autores
from django.urls import reverse_lazy

class HomePageView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name='Listado'
    
class MangaPageView(ListView):
    template_name = 'mangas.html'
    model = Post
    context_object_name='Listado'

class RevistaPageView(ListView):
    template_name = 'revistas.html'
    model = Post
    context_object_name='Listado'

class Descrip_libPageView(ListView):
    template_name = 'descrip_lib.html'
    model = DescripLib
    context_object_name='Listado1'

class AutoresPageView(ListView):
    template_name = 'Autores.html'
    model = Autores
    context_object_name='Listado1'

class DetallePageView(DetailView):
    template_name = 'descAutores.html'
    model = Autores
    context_object_name='Blogs'

class CrearPageView(CreateView):
    template_name = 'CrearAutores.html'
    model = Autores
    fields = '__all__'

class UpdatePageView(UpdateView):
      template_name = 'editarAutores.html'
      model = Autores
      fields = '__all__'

class DeletePageView(DeleteView):
    template_name = 'eliminarAutores.html'
    model = Autores
    context_object_name='Blogs'
    success_url = reverse_lazy('home')