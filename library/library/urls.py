from django.contrib import admin
from django.urls import path, include
from .views import (home_view, books_on_hands_view, take_book_view, deals_history,
                    my_books, return_book, readers_list, bad_readers_list)


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),

    path('auth/', include('authentication.urls', namespace='authentication')),
    path('api/', include('api.urls', namespace='api')),

    path('books_on_hands/', books_on_hands_view, name='books_on_hands'),

    path('my_books/', my_books, name='my_books'),
    path('take_book/', take_book_view, name='take_book'),
    path('return_book/', return_book, name='return_book'),

    path('deals_history/', deals_history, name='deals_history'),
    path('readers_list/', readers_list, name='readers_list'),
    path('bad_readers_list/', bad_readers_list, name='bad_readers_list'),
]
