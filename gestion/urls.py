from django.urls import path
from .views import ProjectView

urlpatterns = [
    path('proyectos/', ProjectView.as_view(), name='lista_proyectos'),
    path('proyectos/<int:pk>/', ProjectView.as_view(), name='detalle_proyecto'),
]