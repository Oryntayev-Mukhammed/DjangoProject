from django import template
from ..models import *

register = template.Library()


@register.simple_tag()
def get_terms(filter=None):
    if filter == None:
        return Terms.objects.all()
    else:
        return Terms.objects.filter(pk=filter)

@register.simple_tag()
def get_person(filter=None):
    if filter == None:
        return Person.objects.all()
    else:
        return Person.objects.filter(pk=filter)
