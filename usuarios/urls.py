from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.Login, name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'usuarios/logout.html'), name='logout')
]
