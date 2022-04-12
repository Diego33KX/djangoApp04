from django.urls import URLPattern, path

from . import views

app_name = 'votaciones'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_region>/', views.list_candidatos, name="list_candidatos"),
    path('<int:id_candidato>/detalle_candidato', views.detalle_candidato, name="detalle_candidato"),
]

