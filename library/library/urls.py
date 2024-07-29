from django.contrib import admin
from django.urls import path, include
from .views import home_view, books_on_hands_view, take_book, deals_history

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('books_on_hands/', books_on_hands_view, name='books_on_hands'),
    path('take_book/', take_book, name='take_book'),
    path('deals_history/', deals_history, name='deals_history'),
    path('api/', include('authentication.urls', namespace='authentication')),
]
