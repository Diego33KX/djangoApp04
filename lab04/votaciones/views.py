from multiprocessing import context
from select import select
from django.shortcuts import get_object_or_404, render
from .models import Region, Candidato
# Create your views here.

def index(request):
    lista_regiones = Region.objects.all()
    context={
        'lista_regiones': lista_regiones
    }
    return render(request, 'votaciones/index.html', context)

def list_candidatos(request, id_region):
    #lista_candidatos = Candidato.objects.filter(region_id=id_region)
    lista_candidatos = get_object_or_404(Region,pk=id_region)
    context={
        'lista_candidatos': lista_candidatos
    }
    return render(request, 'votaciones/candidatos.html', context)

def detalle_candidato(request, id_candidato):
    detalles_candidato = get_object_or_404(Candidato, pk=id_candidato)
    return render(request, 'votaciones/detalle_candidato.html',{'detalles_candidato':detalles_candidato})


