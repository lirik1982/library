from django.contrib import admin

from .models import Book, Deal


class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year')

admin.site.register(Book, BookModelAdmin)
admin.site.register(Deal)
