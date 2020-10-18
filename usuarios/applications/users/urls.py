from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('crear-usuario/', views.CrearUsuarioView.as_view(), name='crear_usuario'),
    path('crear-usuario2/', views.CrearUsuario2View.as_view(), name='crear_usuario2'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('correcto/', views.CorrectoView.as_view(), name='correcto'),
]

