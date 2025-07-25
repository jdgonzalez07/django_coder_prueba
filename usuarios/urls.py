from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.Login, name = 'login'),
    path('registro/', views.registro, name = 'registro'),
    path('perfil/editar/', views.editar_perfil, name = 'editar_perfil'),
    path('logout/', LogoutView.as_view(template_name = 'usuarios/logout.html'), name='logout'),
    
]
