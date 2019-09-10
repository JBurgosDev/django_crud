from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from crud.forms import PersonasForm
from crud.models import PersonasDatos


def listar(request, template_name='index.html'):
    if request.method == 'GET':
        datos = PersonasDatos.objects.all()
        return render(request, template_name, {'datos': datos})


def guardar(request):
    if request.method == 'GET':
        return render(request, 'guardar.html')
    if request.method == 'POST':
        try:
            datos = PersonasForm(request.POST)
            if datos.is_valid():
                datos.save()
                messages.success(request, 'Dato Guardado')
                return redirect('listar')
            else:
                return JsonResponse({'Message': 'Error al guardar datos'})
        except Exception as err:
            return HttpResponse(err)


def eliminar(request, id):
    try:
        datos = PersonasDatos.objects.get(id=id)
        datos.delete()
        messages.add_message(request, messages.WARNING, 'Dato eliminado')
        return redirect('listar')
    except Exception as err:
        return JsonResponse({'datos:' 'dato'})


def actualizar_view(request, id, template_name='actualizar.html'):
    if request.method == 'GET':
        datos = PersonasDatos.objects.get(id=id)
        return render(request, template_name, {'datos': datos})
    if request.method == 'POST':
        try:
            datos = PersonasDatos.objects.get(id=id)
            datos_nuevos = PersonasForm(request.POST, instance=datos)
            if datos_nuevos.is_valid():
                datos_nuevos.save()
                messages.success(request, f'Dato modificado por: {datos.nombre}')
                return redirect('listar')
            else:
                return JsonResponse({'Message' 'Error al modificar'})
        except Exception as err:
            return HttpResponse(err)


def tarea_lista(request, id):
    dato = PersonasDatos.objects.get(id=id)
