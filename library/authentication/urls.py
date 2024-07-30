from django.urls import path
from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView,
    register_view, login_view, logout_view, information_view, permission_deni_view
)

app_name = 'authentication'
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('information/', information_view, name='information'),
    path('permission_deni_view/', permission_deni_view, name='permission_deni_view'),

    path('api/user/', UserRetrieveUpdateAPIView.as_view(), name='api_update'),
    path('api/users/', RegistrationAPIView.as_view(), name='api_register'),
    path('api/users/login/', LoginAPIView.as_view(), name='api_login'),
]
