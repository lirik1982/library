from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'full_name', 'phone', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким именем не найден.")
        if password != cleaned_data.get('password'):
            raise forms.ValidationError("Пароли не совпадают.")
        return cleaned_data
