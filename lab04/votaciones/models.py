from django.db import models
from django.forms import CharField

# Create your models here.
class Region(models.Model):
    nombre_reg = models.CharField(max_length=20)

class Candidato(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    nombre_cand = models.CharField(max_length=20)
    apellido_cand = models.CharField(max_length=20)
    edad_cand = models.IntegerField(max_length=2)
    origen_cand = models.CharField(max_length=15)
    fecha_nacimiento = models.DateTimeField('date of birth')
    partido = models.CharField(max_length=15)



