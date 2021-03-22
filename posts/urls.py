from django.urls import path
from .views import HomePageView,RevistaPageView,MangaPageView,Descrip_libPageView,AutoresPageView,DetallePageView,CrearPageView,UpdatePageView,DeletePageView

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
     path('mangas',RevistaPageView.as_view(),name='mangas'),
      path('revistas',MangaPageView.as_view(),name='revistas'),
      path('descrip',Descrip_libPageView.as_view(),name='descrip'),
      path('Autor',AutoresPageView.as_view(),name='Autores'),
       path('Nombre/<int:pk>/editar',DetallePageView.as_view(),name='descAutores'),
    path('Nuevo/Autor',CrearPageView.as_view(),name='CrearAutores'),
     path('Nombre/<int:pk>/Update',UpdatePageView.as_view(),name='EditAutores'),
      path('Nombre/<int:pk>/delet',DeletePageView.as_view(),name='deleteAutores'),


    
]
