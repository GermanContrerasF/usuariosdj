from django import forms
from django.contrib.auth import authenticate
from .models import User


class UserForm(forms.ModelForm):

    password = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'contraseña'}
    ))
    password2 = forms.CharField(label='Repetir Contraseña', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'repetir contraseña'}
    ))

    def clean_password2(self):
        data = self.cleaned_data
        password = data.get('password', None)
        password2 = data.get('password2', None)

        if password and password2:
            if password != password2:
                # raise forms.ValidationError('Las contraseñas indicadas no son iguales')
                self.add_error('password2', 'Las contraseñas no son iguales')

            if len(password2) < 5:
                self.add_error('password2', 'El largo de la contraseña debe ser de 5 o mas caracteres')

        return data['password2']

    class Meta:
        model = User
        fields = ['username', 'email', 'nombres', 'apellidos', 'genero']


class LoginForm(forms.Form):
    ''' LoginForm '''
    username = forms.CharField(label='Usuario', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Usuario'}
    ))
    password = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Contraseña'}
    ))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Datos indicados no validos')

        return cleaned_data
