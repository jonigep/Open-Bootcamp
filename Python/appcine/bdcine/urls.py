from django.urls import path

from . import views

urlpatterns = [
  path('', views.directores, name='index'),
  path('<nombre_director>/', views.direct, name='director'),
  path('pelicula/<pelicula>/', views.infopelicula, name='pelicula'),

]