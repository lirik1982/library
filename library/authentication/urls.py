# from django.urls import path, include
# from .views import register_view, login_view, logout_view
#
# urlpatterns = [
#     path('register/', register_view, name='register'),
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
# ]

from django.urls import path
from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView
)

app_name = 'authentication'
urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view(), name='update'),
    path('users/', RegistrationAPIView.as_view(), name='register'),
    path('users/login/', LoginAPIView.as_view(), name='login'),
]
