from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Directores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField()

    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directores'

    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)

class Peliculas(models.Model):
    nombre = models.CharField(max_length=60)
    agno_estreno = models.PositiveIntegerField(verbose_name='Año de Estreno',default=1950,validators=[MinValueValidator(1895)])
    director = models.ForeignKey('Directores', on_delete=models.CASCADE)
    sinopsis = models.TextField()

    class Meta:
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'

    def __str__(self):
        return self.nombre
