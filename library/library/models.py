from django.conf import settings
from django.db import models


user = settings.AUTH_USER_MODEL

GENRES = {
    'научная фантастика': 'science fiction',
    'детектив': 'detective',
    'роман': 'novel',
    'фэнтези': 'fantasy',
    'научная': 'scince',
}


class Book(models.Model):
    title = models.CharField(max_length=150, unique=False)
    author = models.CharField(max_length=100, unique=False)
    year = models.IntegerField(unique=False)
    genre = models.CharField(max_length=100, choices=GENRES.items())
    available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.year) + ' ' + self.author + ' ' + self.title


class Deal(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(user, on_delete=models.CASCADE)
    date_taken = models.DateTimeField(null=True, blank=True)
    date_get_back = models.DateTimeField(null=True, blank=True)


