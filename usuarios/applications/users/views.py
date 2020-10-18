from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, CreateView, TemplateView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import User
from .forms import UserForm, LoginForm


class CrearUsuarioView(CreateView):
    template_name = 'users/crear_usuario.html'
    form_class = UserForm
    model = User
    # fields = ['username', 'email', 'password']
    success_url = reverse_lazy('users_app:correcto')


class CrearUsuario2View(FormView):
    template_name = 'users/crear_usuario.html'
    form_class = UserForm
    success_url = reverse_lazy('users_app:correcto')

    # para que esta vista pueda guardar
    # se debe sobreescribir el metodo form_valid()
    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        nombres = form.cleaned_data['nombres']
        apellidos = form.cleaned_data['apellidos']
        genero = form.cleaned_data['genero']
        password = form.cleaned_data['password']

        User.objects.create_user(
            username,
            email,
            password,
            nombres=nombres,
            apellidos=apellidos,
            genero=genero
        )

        return super(CrearUsuario2View, self).form_valid(form)


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:panel')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )

        login(self.request, user)
        return super(LoginView, self).form_valid(form)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('users_app:login'))


class CorrectoView(TemplateView):
    template_name = 'correcto.html'
