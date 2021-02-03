from django.contrib import admin
from .models import *
from django.forms import TextInput, Select


class PersonalManagerInline(admin.TabularInline):
    model = PersonalManager
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'style': 'width: 20'})}
    }
    extra = 0
    max_num = 1


class VisaInline(admin.TabularInline):
    model = VisaCity
    fields = ('date', 'pass_visa_date', 'present_visa_date', 'guest_come_date', 'guest_back_date', 'employee',
              'payment_type', 'status')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'style': 'width: 20'})},
    }
    extra = 0
    max_num = 1


class AirTicketInline(admin.StackedInline):
    model = AirTicket
    fields = (('date', ), ('guest_full_name_visa', 'citizen', 'trip_goal', 'flight'),
              ('country', 'carrier', 'employee', 'ticket_office',),
              ('flight_come_date', 'flight_back_date', 'price', 'payment_type'))
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'style': 'width: 150px'})},
        models.ForeignKey: {'widget': Select(attrs={'style': 'width: 130px'})},
    }
    extra = 0
    max_num = 1


class HotelInline(admin.TabularInline):
    model = Hotel
    fields = ('date', 'hotel_name', 'guest_come_date', 'guest_back_date', 'employee',
              'price', 'payment_type')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'style': 'width: 20'})}
    }
    extra = 0
    max_num = 1


class OtherDocumentInline(admin.TabularInline):
    model = OtherDocument
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'style': 'width: 20'})}
    }
    extra = 0
    max_num = 1


class VisaControlInline(admin.TabularInline):
    model = VisaControl
    fields = ('date', 'employee', 'guest_come_date', 'guest_back_date', 'guest_living_address',
              'guest_living_address_type', 'registration_date', 'visa_validate_date', 'license_date',
              'possible_leave_date', 'guest_status')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'style': 'width: 20'})}
    }
    extra = 0
    max_num = 1
