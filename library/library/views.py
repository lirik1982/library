from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from authentication.models import User
from .models import Book, Deal
from django.db.models import F, Q


def home_view(request):
    context = {
        'books': Book.objects.filter(available=True)
    }
    return render(request, 'books_list.html', context)


def books_on_hands_view(request):
    unavailable_books = Book.objects.filter(available=False).annotate(
        date_taken=F('deal__date_taken'),
    ).values('date_taken')

    context = {
        'books': unavailable_books,
    }
    return render(request, 'books_on_hands.html', context)


def deals_history(request):
    deals = Deal.objects.select_related('book', 'reader').annotate(
        title=F('book__title'),
        author=F('book__author'),
        year=F('book__year'),
        reader_name=F('reader__full_name'),
        reader_phone=F('reader__phone'),
    ).values('title', 'author', 'year', 'reader_name', 'date_taken', 'reader_phone', 'date_get_back')

    context = {
        'deals': deals,
    }
    return render(request, 'deals_history.html', context)


def take_book(request):
    if request.method == 'POST':
        # books = Book.objects.all()
        # for book in books:
        #     book.available = True
        #     book.save()

        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, id=book_id)
        if book.available:
            user = request.user

            deal = Deal(
                book=book,
                reader=user,
                date_taken=timezone.now(),
                date_get_back=None
            )
            deal.save()

            book.available = False
            book.save()
            return HttpResponse('Есть выдача', status=200)
        else:
            return HttpResponse('Ошибка', status=400)


