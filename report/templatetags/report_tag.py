import logging

from django import template

register = template.Library()


@register.simple_tag
def get_airticket(qs):
    try:
        ticket = qs.values_list('total')
        t = 0
        for i in ticket:
            if i[0] is not None:
                t += i[0]
    except Exception as e:
        logging.error(str(e))
    else:
        return t


@register.simple_tag
def get_ticket(qs):
    try:
        ticket = qs.values_list('company_offered__personal_manager__guest__airtickets__price')
        t = 0
        for i in ticket:
            if i[0] is not None:
                t += i[0]
    except Exception as e:
        logging.error(str(e))
    else:
        return t


@register.simple_tag
def get_hotel(qs):
    try:
        hotel = qs.values_list('company_offered__personal_manager__guest__hotels__price')
        t = 0
        for i in hotel:
            if i[0] is not None:
                t += i[0]
    except Exception as e:
        logging.error(str(e))
    else:
        return t


@register.simple_tag
def get_visa(qs):
    try:
        visa = qs.values_list('company_offered__personal_manager__guest__others__price')
        t = 0
        for i in visa:
            if i[0] is not None:
                t += i[0]
    except Exception as e:
        logging.error(str(e))
    else:
        return t


@register.simple_tag
def get_reg(qs):
    try:
        reg = qs.values_list('company_offered__personal_manager__guest__regs')
        t = 0
        for i in reg:
            if i[0] is not None:
                t += 300000
    except Exception as e:
        logging.error(str(e))
    else:
        return t

