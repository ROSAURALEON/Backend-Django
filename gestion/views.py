
import json

from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Project


@method_decorator(csrf_exempt, name='dispatch')
class ProjectView(View):

    # Consultar todos los proyectos
    def get(self, request):
        proyectos = Project.objects.all()

        datos = []

        for proyecto in proyectos:
            datos.append({
                "id": proyecto.id,
                "name": proyecto.name,
                "description": proyecto.description,
                "start_date": proyecto.start_date
            })

        return JsonResponse(datos, safe=False)

    # Crear un proyecto
    def post(self, request):
        try:
            datos = json.loads(request.body)

            proyecto = Project.objects.create(
                name=datos["name"],
                description=datos["description"],
                start_date=datos["start_date"]
            )

            return JsonResponse({
                "mensaje": "Proyecto creado correctamente",
                "id": proyecto.id
            }, status=201)

        except (json.JSONDecodeError, KeyError, ValueError):
            return JsonResponse({
                "error": "Los datos enviados no son válidos"
            }, status=400)

    # Actualizar un proyecto
    def put(self, request, pk):
        try:
            proyecto = Project.objects.get(pk=pk)
            datos = json.loads(request.body)

            proyecto.name = datos["name"]
            proyecto.description = datos["description"]
            proyecto.start_date = datos["start_date"]

            proyecto.save()

            return JsonResponse({
                "mensaje": "Proyecto actualizado correctamente"
            })

        except Project.DoesNotExist:
            return JsonResponse({
                "error": "El proyecto no existe"
            }, status=404)

        except (json.JSONDecodeError, KeyError, ValueError):
            return JsonResponse({
                "error": "Los datos enviados no son válidos"
            }, status=400)

    # Eliminar un proyecto
    def delete(self, request, pk):
        try:
            proyecto = Project.objects.get(pk=pk)
            proyecto.delete()

            return JsonResponse({
                "mensaje": "Proyecto eliminado correctamente"
            })

        except Project.DoesNotExist:
            return JsonResponse({
                "error": "El proyecto no existe"
            }, status=404)
