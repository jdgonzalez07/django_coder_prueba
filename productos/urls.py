from django.urls import path
# from .views import sartenes
from productos import views

app_name = 'productos'

urlpatterns = [
    path('sartenes/', views.Sartenes.as_view(), name='listado_de_sartenes'),
    path('sartenes/crear/', views.CrearSarten.as_view(), name='crear_sarten'),
    path('sartenes/<int:pk>/', views.VerSarten.as_view(), name='ver_sarten'),
    path('sartenes/<int:pk>/eliminar/', views.Sartenes.as_view(), name='eliminar_sarten'),
    path('sartenes/<int:pk>/actualizar/', views.ActualizarSarten.as_view(), name='actualizar_sarten'),
    
]
