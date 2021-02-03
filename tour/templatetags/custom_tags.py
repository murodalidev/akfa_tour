from django import template
from django.db.models import Q
from django.db.models.aggregates import Sum

register = template.Library()


@register.simple_tag
def get_total_uzs(qs):
    try:
        return qs.filter(Q(payment_type='transfer') | Q(payment_type='not_payed')
                         ).aggregate(tot=Sum('price'))['tot']
    except:
        pass


@register.simple_tag
def get_total_usd(qs):
    try:
        return qs.filter(Q(payment_type='transfer') | Q(payment_type='not_payed')
                         ).aggregate(tot=Sum('price_us'))['tot']
    except:
        pass


@register.simple_tag
def call_method(obj, method_name, *args):
    method = getattr(obj, method_name)
    return method(*args)
