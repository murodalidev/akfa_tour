from django.contrib import admin
from .models import *
from django.forms import Textarea, TextInput
from rangefilter.filter import DateRangeFilter
from tabular_export.admin import export_to_excel_action


class PersonalManagerInline(admin.TabularInline):
    model = PersonalManager
    # fields = (('personal_manager', 'company_offered', 'personal_manager_phone'),)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'style': 'width: 20'})}
    }
    extra = 0


class VisaInline(admin.TabularInline):
    model = VisaCity
    # fields = (('employee', 'pass_visa_date', 'present_visa_date', 'from_visa_submitted_date'),
    #           ('visa_price_uzs', 'visa_price_us', 'payment_type_to_visa'))
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'style': 'width: 20'})},
    }
    extra = 0


class AirTicketInline(admin.TabularInline):
    model = AirTicket
    # fields = (
    #     'guest', ('guest_full_name_visa', 'citizen', 'trip_goal'), ('flight', 'flight_come_date', 'flight_back_date'),
    #     ('carrier', 'ticket_price'), ('personal_manager_for_payment', 'payment_type_to_ticket'))
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'style': 'width: 20'})}
    }
    extra = 0


class HotelInline(admin.TabularInline):
    model = Hotel
    # fields = ('guest', 'hotel_name', ('guest_come_to_hotel_date', 'guest_back_to_hotel_date'),
    #           ('hotel_price_uzs', 'hotel_price_us', 'guest_living_days', 'payment_type_to_hotel'))
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'style': 'width: 20'})}
    }
    extra = 0


class OtherDocumentInline(admin.TabularInline):
    model = OtherDocument
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'style': 'width: 20'})}
    }
    extra = 0


class VisaControlInline(admin.TabularInline):
    model = VisaControl
    # fields = ('guest', ('guest_living_address', 'guest_living_address_type', 'registration_date'), ('guest_come_date',
    #                                                                                                 'guest_back_date',
    #                                                                                                 'license_date',
    #                                                                                                 'possible_leave_date'),
    #           ('note', 'visa_validate_date', 'guest_status'))
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'style': 'width: 20'})}
    }
    extra = 0
