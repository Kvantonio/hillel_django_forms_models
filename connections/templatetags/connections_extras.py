import json
import re

from connections.models import Quote

from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag
def random_quote():
    t = Quote.objects.order_by('?').first()
    a = ('<h4 align="right">Random quote</h4><p align="right">'
         + str(t) + '</p><p align="right">'
         + str(t.creator) + '</p>')
    return mark_safe(a)


@register.filter(name='no_swear')
def swear(value):
    with open('./word.json', 'r') as f:
        data = json.load(f)

        for i in data:
            temp = re.sub(r'\b' + i + r'\b', '***', str(value))
            value = temp
        result = value
    return result
