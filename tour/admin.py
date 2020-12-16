from django.utils.html import format_html

from .admin_inline import *
from datetime import datetime


class GuestInfoAdmin(admin.ModelAdmin):
    inlines = (PersonalManagerInline, VisaInline, AirTicketInline, HotelInline, OtherDocumentInline, VisaControlInline)
    list_display = ('guest_full_name', 'passport_id', 'citizenship', 'foreign_company', 'created_date')
    actions = (export_to_excel_action,)
    list_per_page = 100


class PersonalManagerAdmin(admin.ModelAdmin):
    list_display = ('date', 'guest', 'company_offered', 'personal_manager', 'personal_manager_phone')
    # fields = ('personal_manager', 'company_offered', 'personal_manager_phone', 'guest', 'created_date')
    search_fields = ('guest', 'personal_manager', 'personal_manager_phone', 'company_offered')
    list_filter = ('company_offered',)
    list_per_page = 100


class VisaCityAdmin(admin.ModelAdmin):
    list_display = ('date', 'guest', 'get_foreign_company', 'get_company_offered', 'pass_visa_date', 'present_visa_date',
                    'guest_come_date', 'guest_back_date', 'get_passport', 'get_citizenship',
                    'employee', 'payment_type_to_visa', 'get_days', 'get_status')
    search_fields = ('guest__guest_full_name',)
    list_filter = ( # ('pass_visa_date', DateRangeFilter), ('present_visa_date', DateRangeFilter),
                   'date', 'payment_type_to_visa', 'employee')
    list_per_page = 100

    def get_days(self, obj):
        if obj.present_visa_date and not obj.guest_come_date:
            date = datetime.today().date() - obj.present_visa_date
            return date.days, 'kun'
        if obj.guest_come_date:
            return 'E\'tibor bermang'
        return 'Visa taqdim etilgan sana kiritilmagan'
    get_days.short_description = 'Visa olingan kundan'

    def get_status(self, obj):
        if obj.guest_come_date and obj.guest_back_date:
            return 'Qaytib ketti'
        elif not obj.guest_come_date and not obj.guest_back_date:
            return 'Kelmadi'
        elif obj.guest_come_date and not obj.guest_back_date:
            return 'Keldi'
        elif not obj.guest_come_date and obj.guest_back_date:
            return format_html(
                '<div style="background-color: #C00; color: #fff; padding: 5px;">Mehmon kelgan sanani kiriting!</div>')


class AirTicketAdmin(admin.ModelAdmin):
    list_display = ('date', 'guest_full_name_visa', 'citizen', 'get_company_offered', 'get_personal_manager',
                    'trip_goal', 'flight', 'country', 'employee', 'ticket_office', 'flight_come_date',
                    'flight_back_date', 'carrier', 'ticket_price', 'payment_type_to_ticket')
    list_display_links = ('guest_full_name_visa',)
    search_fields = ('guest__guest_full_name', 'flight', 'country__country_name')
    list_filter = ('date', 'citizen', 'payment_type_to_ticket', 'employee')
    list_per_page = 100


class HotelAdmin(admin.ModelAdmin):
    list_display = ('date', 'guest', 'get_citizenship', 'get_company_offered', 'get_personal_manager', 'hotel_name',
                    'guest_come_date', 'guest_back_date', 'employee', 'hotel_price_uzs', 'hotel_price_us', 'get_days',
                    'payment_type_to_hotel')
    list_display_links = ('guest', 'hotel_name')
    search_fields = ('guest__guest_full_name', 'hotel_name')
    list_filter = (  # ('guest_come_to_hotel_date', DateRangeFilter), ('guest_back_to_hotel_date', DateRangeFilter),
        'date', 'guest_come_date', 'guest_back_date', 'payment_type_to_hotel', 'employee')
    list_per_page = 100

    def get_days(self, obj):
        if obj.guest_come_date and not obj.guest_back_date:
            date = datetime.today().date() - obj.guest_come_date
            return date.days, 'kun'
        elif obj.guest_come_date and obj.guest_back_date:
            date = obj.guest_back_date - obj.guest_come_date
            return date.days, 'kun'
    get_days.short_description = 'Yashagan kunlari'


class OtherDocumentAdmin(admin.ModelAdmin):
    list_display = ('date', 'guest', 'get_citizenship', 'get_company_offered', 'get_trip_goal', 'visa_price_uzs',
                    'visa_price_us', 'employee', 'payment_type_to_visa')
    list_display_links = ('guest',)
    search_fields = ('guest__guest_full_name', 'hotel_name')
    list_filter = (  # ('guest_come_to_hotel_date', DateRangeFilter), ('guest_back_to_hotel_date', DateRangeFilter),
        'date', 'payment_type_to_visa',  'employee')
    list_per_page = 100


class VisaControlAdmin(admin.ModelAdmin):
    list_display = ('date', 'guest', 'employee', 'get_company_offered', 'get_citizenship', 'guest_come_date',
                    'guest_back_date', 'guest_living_address', 'guest_living_address_type', 'registration_date',
                    'visa_validate_date', 'license_date', 'possible_leave_date', 'note', 'get_personal_manager',
                    'guest_status', 'get_visa_days')
    list_display_links = ('guest',)
    search_fields = ('guest__guest_full_name', 'employee', 'guest_living_address')
    list_filter = ('date', 'guest_living_address_type', 'guest_status')
    list_per_page = 100

    def get_visa_days(self, obj):
        if obj.visa_validate_date:
            date = obj.visa_validate_date - datetime.today().date()
            if date.days <= 20:
                return format_html('<div style="background-color: #CC0000; color: #fff; padding: 5px;"> {} </div>'
                                   .format(date.days))
            return date.days, 'kun'
        return 'Amal qilish muddati kiritilmagan'
    get_visa_days.short_description = 'Kunlar soni'


admin.site.register(GuestInfo, GuestInfoAdmin)
admin.site.register(PersonalManager, PersonalManagerAdmin)
admin.site.register(VisaCity, VisaCityAdmin)
admin.site.register(AirTicket, AirTicketAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(OtherDocument, OtherDocumentAdmin)
admin.site.register(VisaControl, VisaControlAdmin)

admin.site.site_header = 'Akfa Tour'
