from django import template
from django.utils.safestring import mark_safe
import locale

register = template.Library()

@register.filter(name='decimalcomma')
def decimalcomma(value):
    try:
        locale.setlocale(locale.LC_ALL, '')
        return mark_safe(locale.format('%.2f', value, grouping=True))
    except (ValueError, locale.Error):
        return value