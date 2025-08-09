# recetas/views.py
from django.shortcuts import render, get_object_or_404
from .models import Receta, Paciente
from django.core.paginator import Paginator
from django.shortcuts import render


def home(request):
    return render(request, 'recetas/home.html')



def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    tips = receta.tips.all()
    return render(request, 'recetas/detalle_receta.html', {'receta': receta, 'tips': tips})



def lista_recetas(request):
    categoria = request.GET.get('categoria')
    tiempo_max = request.GET.get('tiempo_max')
    porciones_min = request.GET.get('porciones_min')
    porciones_max = request.GET.get('porciones_max')

    """ recetas = Receta.objects.all() """
    recetas = Receta.objects.filter(activa=True)

    if categoria:
        recetas = recetas.filter(categoria=categoria)
    if tiempo_max:
        recetas = recetas.filter(tiempo_preparacion__lte=tiempo_max)
    if porciones_min:
        recetas = recetas.filter(porciones__gte=porciones_min)
    if porciones_max:
        recetas = recetas.filter(porciones__lte=porciones_max)

    paginator = Paginator(recetas, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recetas/lista_recetas.html', {
        'recetas': page_obj,
        'page_obj': page_obj,
        'categoria_actual': categoria,
        'tiempo_max': tiempo_max,
        'porciones_min': porciones_min,
        'porciones_max': porciones_max
    })

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'recetas/lista_pacientes.html', {'pacientes': pacientes})