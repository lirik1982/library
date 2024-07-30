import datetime

from datetime import datetime, timedelta
from django import template
from django.utils.timesince import timesince
from django.utils import timezone

register = template.Library()
days_for_book_handlers = 14

@register.filter
def days_until(value):
    now = timezone.now()
    try:
        difference = abs((now - value).days)
    except Exception as e:
        return value

    if difference > days_for_book_handlers:
        return 'Просрочено на {} дней'.format(difference - days_for_book_handlers)

    return 'Ожидается {}'.format((value + timedelta(days=days_for_book_handlers)).strftime('%d/%m/%Y'))
