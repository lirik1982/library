from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'full_name', 'phone', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким именем не найден.")
        if password != cleaned_data.get('password'):
            raise forms.ValidationError("Пароли не совпадают.")
        return cleaned_data
