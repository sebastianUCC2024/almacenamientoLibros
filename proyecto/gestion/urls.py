from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear/', views.crear_autor, name='crear_autor'),
    path('autores/editar/<int:pk>/', views.editar_autor, name='editar_autor'),
    path('autores/eliminar/<int:pk>/', views.eliminar_autor, name='eliminar_autor'),

    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/editar/<int:pk>/', views.editar_libro, name='editar_libro'),
    path('libros/eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),

    path('gen/autores/', views.AutorListView.as_view(), name='autor_list'),
    path('gen/autores/crear/', views.AutorCreateView.as_view(), name='autor_create'),
    path('gen/autores/editar/<int:pk>/', views.AutorUpdateView.as_view(), name='autor_update'),
    path('gen/autores/eliminar/<int:pk>/', views.AutorDeleteView.as_view(), name='autor_delete'),

    path('gen/libros/', views.LibroListView.as_view(), name='libro_list'),
    path('gen/libros/crear/', views.LibroCreateView.as_view(), name='libro_create'),
    path('gen/libros/editar/<int:pk>/', views.LibroUpdateView.as_view(), name='libro_update'),
    path('gen/libros/eliminar/<int:pk>/', views.LibroDeleteView.as_view(), name='libro_delete'),
    path('', views.inicio, name='inicio'),
]