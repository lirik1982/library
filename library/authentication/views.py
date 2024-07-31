from functools import wraps

from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


def register_view(request):
    if request.method == 'POST':
        if request.POST['password1'] != request.POST['password2']:
            return redirect('home')

        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('home')


def information_view(request):
    return render(request, 'information.html')


def permission_deni_view(request):
    return render(request, 'permission_deni.html')


def check_auth(function=None):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('authentication:information')
        return wrapper
    return decorator if function is None else decorator(function)


def check_is_librarian(function=None):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role == 'librarian':
                return view_func(request, *args, **kwargs)
            else:
                return redirect('authentication:permission_deni_view')
        return wrapper
    return decorator if function is None else decorator(function)
