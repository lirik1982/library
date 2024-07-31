import datetime

from django.db import models
from django.db.models.functions import ExtractDay
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Book, Deal
from django.db.models import F, Count, Q
from authentication.models import User
from authentication.views import check_auth, check_is_librarian


def home_view(request):
    context = {
        'books': Book.objects.filter(available=True).order_by('title')
    }
    return render(request, 'books_list.html', context)


@check_auth
def books_on_hands_view(request):

    # sqlite не делает distinct
    # unavailable_books = Book.objects.filter(available=False).annotate(
    #     date_taken=F('deal__date_taken'),
    # ).values('title', 'author', 'date_taken', 'year', 'date_taken', 'genre'
    #          ).order_by('-date_taken'
    #                     ).distinct('title') #TODO

    unavailable_books = (Book.objects.filter(available=False).
                         values('title', 'author', 'year', 'genre'))

    context = {
        'books': unavailable_books,
    }
    return render(request, 'books_on_hands.html', context)


@check_is_librarian
def deals_history(request):
    deals = Deal.objects.select_related('book', 'reader').annotate(
        title=F('book__title'),
        author=F('book__author'),
        year=F('book__year'),
        reader_name=F('reader__full_name'),
        reader_phone=F('reader__phone'),
    ).values('title', 'author', 'year', 'reader_name', 'date_taken', 'reader_phone', 'date_get_back').order_by(
        '-date_taken')

    context = {
        'deals': deals,
    }
    return render(request, 'deals_history.html', context)


def take_book(book_id, user):
    book = get_object_or_404(Book, id=book_id)
    if book.available:
        deal = Deal(
            book=book,
            reader=user,
            date_taken=timezone.now(),
            date_get_back=None
        )
        deal.save()
        book.available = False
        book.save()
        return True
    else:
        return False


def take_book_view(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        if take_book(book_id, request.user):
            return HttpResponse('Есть выдача', status=200)
    return HttpResponse('Ошибка', status=400)


@check_auth
def my_books(request):
    user = request.user
    deals = (Deal.objects.filter(reader=user).select_related('book', 'reader').annotate(
        title=F('book__title'),
        author=F('book__author'),
        year=F('book__year'),
        reader_name=F('reader__full_name'),
        reader_phone=F('reader__phone'),
    ).values('id', 'title', 'author', 'year', 'reader_name', 'date_taken', 'reader_phone', 'date_get_back').
             order_by('-date_taken'))
    context = {
        'deals': deals,
    }
    return render(request, 'my_books.html', context)


def return_book(request):
    if request.method == 'POST':
        deal_id = request.POST.get('deal_id')
        deal = get_object_or_404(Deal, id=deal_id)
        book = get_object_or_404(Book, id=deal.book.id)
        try:
            deal.date_get_back = timezone.now()
            book.available = True
            deal.save(update_fields=['date_get_back'])
            book.save(update_fields=['available'])
        except Exception as e:
            return HttpResponse('Ошибка', status=400)
        else:
            return HttpResponse('Возвращена', status=200)


@check_is_librarian
def readers_list(request):
    readers = User.objects.filter(role='reader')
    return render(request, 'readers_list.html', {'readers': readers})


@check_is_librarian
def bad_readers_list(request):
    readers_with_books = Deal.objects.filter(date_get_back__isnull=True).annotate(
        username=F('reader__username'),
        fullname=F('reader__full_name'),
        phone=F('reader__phone'),
        address=F('reader__address'),

        title=F('book__title'),
        author=F('book__author'),
    ).values(
        'username', 'fullname', 'address', 'phone', 'title', 'date_taken'
    )
    return render(request, 'readers_with_books.html', {'readers': readers_with_books})
