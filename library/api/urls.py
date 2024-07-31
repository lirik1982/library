from django.urls import path
from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView, GetAllBooksAPIView,
    TakeBookAPIView, ReturnBookAPIView, BooksOnHandsListAPIView
)

app_name = 'api'
urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view(), name='api_update'),
    path('users/', RegistrationAPIView.as_view(), name='api_register'),
    path('users/login/', LoginAPIView.as_view(), name='api_login'),

    path('books/', GetAllBooksAPIView.as_view(), name='get_books_list'),
    path('books_on_hands/', BooksOnHandsListAPIView.as_view(), name='books_on_hands'),

    path('take_book/<int:book_id>', TakeBookAPIView.as_view(), name='take_book'),
    path('return_book/<int:book_id>', ReturnBookAPIView.as_view(), name='return_book'),
]
