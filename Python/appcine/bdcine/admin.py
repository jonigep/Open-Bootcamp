from django.contrib import admin
from .models import Directores, Peliculas

# Register your models here.

class PeliculasStacked(admin.StackedInline):
    model = Peliculas
    extra = 0

class DirectoresAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','fecha_nacimiento',)
    search_fields=('nombre','apellido')
    inlines = [PeliculasStacked]

class PeliculasAdmin(admin.ModelAdmin):
    list_display = ('nombre','agno_estreno','director','sinopsis')
    search_fields = ('nombre','director')
    list_filter = ('agno_estreno',)


admin.site.register(Directores,DirectoresAdmin)
admin.site.register(Peliculas,PeliculasAdmin)
