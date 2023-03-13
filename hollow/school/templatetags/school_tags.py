from django import template
from ..models import *

register = template.Library()


@register.simple_tag()
def get_terms():
    return Terms.objects.all()
