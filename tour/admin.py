from django.utils.html import format_html
from .admin_inline import *
from datetime import datetime
from tabular_export.admin import export_to_excel_action, export_to_excel_response


class GuestInfoAdmin(admin.ModelAdmin):
    change_list_template = 'admin/total.html'
    inlines = (PersonalManagerInline, VisaInline, AirTicketInline, HotelInline, OtherDocumentInline, VisaControlInline)
    list_display = ('guest_full_name', 'passport_id', 'citizenship', 'foreign_company', 'created_date')
    search_fields = ('guest_full_name', 'passport_id', 'citizenship__citizenship', 'foreign_company')
    # actions = (export_to_excel_action,)
    list_filter = ('created_date',)
    actions = (export_to_excel_action,)
    list_per_page = 100


class PersonalManagerAdmin(admin.ModelAdmin):
    change_list_template = 'admin/total.html'
    list_display = ('date', 'guest', 'company_offered', 'personal_manager', 'personal_manager_phone')
    search_fields = ('guest__guest_full_name', 'personal_manager', 'personal_manager_phone',
                     'company_offered__company_name')
    list_display_links = ('date', 'guest',)
    list_filter = ('company_offered',)
    autocomplete_fields = ('guest',)
    actions = ('export_batch_summary_action',)
    list_per_page = 100

    def export_batch_summary_action(self, request, queryset):
        headers = ['sana', 'Mehmon', 'Taklif qiluvchi tashkilot', 'Masul shaxs',  'Masul shaxsing raqami']
        rows = queryset.values_list('date', 'guest__guest_full_name', 'company_offered__company_name',
                                    'personal_manager', 'personal_manager_phone')
        return export_to_excel_response('Masul_shaxs.xlsx', headers, rows)

    export_batch_summary_action.short_description = 'Export to excel'


class VisaCityAdmin(admin.ModelAdmin):
    change_list_template = 'admin/total.html'
    list_display = ('date', 'guest', 'get_foreign_company', 'get_company_offered', 'pass_visa_date',
                    'present_visa_date', 'guest_come_date', 'guest_back_date', 'get_passport', 'get_citizenship',
                    'employee', 'payment_type', 'get_days', 'get_status')
    search_fields = ('guest__guest_full_name', 'guest__foreign_company',
                     'guest__personal_managers__company_offered__company_name')
    list_display_links = ('date', 'guest')
    autocomplete_fields = ('guest',)
    list_filter = (  # ('pass_visa_date', DateRangeFilter), ('present_visa_date', DateRangeFilter),
        'date', 'payment_type', 'employee')
    actions = ('export_batch_summary_action', )
    list_per_page = 100

    def export_batch_summary_action(self, request, queryset):
        headers = ['Sana', 'Mehmon', 'Xorijiy tashkilot', 'Taklif qiluvchi tashkilot', 'Visaga topshitilgan sana',
                   'Visa taqdim etilgan sana', 'Mehmon keldi', 'Mehmon ketdi', 'Passport', 'Fuqaroligi', 'Agent',
                   'To\'lov statusi', 'Visa olingan kundan', 'Holati']
        rows = queryset.values_list('date', 'guest__guest_full_name', 'guest__foreign_company',
                                    'guest__personal_managers__company_offered__company_name', 'pass_visa_date',
                                    'present_visa_date', 'guest_come_date', 'guest_back_date', 'guest__passport_id',
                                    'guest__citizenship__citizenship', 'employee__username', 'payment_type', 'visa_days'
                                    , 'status')
        return export_to_excel_response('VisaCity.xlsx', headers, rows)

    export_batch_summary_action.short_description = 'Export to excel'

    def get_days(self, obj):
        if obj.present_visa_date and not obj.guest_come_date:
            date = datetime.today().date() - obj.present_visa_date
            obj.visa_days = str(date.days) + ' kun'
            obj.save()
            return date.days, 'kun'
        if obj.guest_come_date:
            obj.visa_days = 'E\'tibor bermang'
            obj.save()
            return 'E\'tibor bermang'
        return 'Visa taqdim etilgan sana kiritilmagan'

    get_days.short_description = 'Visa olingan kundan'

    def get_status(self, obj):
        if obj.guest_come_date and obj.guest_back_date:
            obj.status = 'Qaytib ketti'
            obj.save()
            return 'Qaytib ketti'
        elif not obj.guest_come_date and not obj.guest_back_date:
            obj.status = 'Kelmadi'
            obj.save()
            return 'Kelmadi'
        elif obj.guest_come_date and not obj.guest_back_date:
            obj.status = 'Keldi'
            obj.save()
            return 'Keldi'
        elif not obj.guest_come_date and obj.guest_back_date:
            obj.status = format_html(
                '<div style="background-color: #C00; color: #fff; padding: 5px;">Mehmon kelgan sanani kiriting!</div>')
            obj.save()
            return format_html(
                '<div style="background-color: #C00; color: #fff; padding: 5px;">Mehmon kelgan sanani kiriting!</div>')

    get_status.short_description = 'Holati'


class AirTicketAdmin(admin.ModelAdmin):
    change_list_template = 'admin/total.html'
    list_display = ('date', 'guest_full_name_visa', 'citizen', 'get_company_offered', 'get_personal_manager',
                    'trip_goal', 'flight', 'country', 'employee', 'ticket_office', 'flight_come_date',
                    'flight_back_date', 'carrier', 'price', 'payment_type')
    list_display_links = ('date', 'guest_full_name_visa',)
    autocomplete_fields = ('guest',)
    list_editable = ('payment_type',)
    search_fields = ('guest__guest_full_name', 'flight', 'country__country',
                     'guest__personal_managers__personal_manager',
                     'guest__personal_managers__company_offered__company_name')
    list_filter = ('date', 'citizen', 'payment_type', 'employee')
    date_hierarchy = 'date'
    actions = ('export_batch_summary_action', )
    list_per_page = 100

    def export_batch_summary_action(self, request, queryset):
        headers = ['Sana', 'Mehmon', 'Fuqaroligi', 'Taklif qiluvchi tashkilot', 'Mas\'ul shaxs', 'Safar maqsadi',
                   'Reys', 'Davlati', 'Agent', 'Aviakassa', 'Kelgan reys', 'Ketgan reys', 'Aviatashuvchi',
                   'Bilet narxi', 'To\'lov statusi']
        rows = queryset.values_list('date', 'guest_full_name_visa', 'citizen',
                                    'guest__personal_managers__company_offered__company_name',
                                    'guest__personal_managers__personal_manager',
                                    'trip_goal', 'flight', 'country', 'employee__username', 'ticket_office',
                                    'flight_come_date', 'flight_back_date', 'carrier__name', 'price', 'payment_type')
        return export_to_excel_response('AirTicket.xlsx', headers, rows)

    export_batch_summary_action.short_description = 'Export to excel'


class HotelAdmin(admin.ModelAdmin):
    change_list_template = 'admin/total.html'
    list_display = ('date', 'guest', 'get_citizenship', 'get_company_offered', 'get_personal_manager', 'hotel_name',
                    'guest_come_date', 'guest_back_date', 'employee', 'price', 'get_days',
                    'payment_type')
    list_display_links = ('date', 'guest', 'hotel_name')
    search_fields = ('guest__guest_full_name', 'guest__personal_managers__personal_manager',
                     'guest__citizenship__citizenship', 'guest__personal_managers__company_offered__company_name')
    list_editable = ('payment_type',)
    autocomplete_fields = ('guest',)
    list_filter = (  # ('guest_come_to_hotel_date', DateRangeFilter), ('guest_back_to_hotel_date', DateRangeFilter),
        'date', 'guest_come_date', 'guest_back_date', 'payment_type', 'employee')
    date_hierarchy = 'date'
    actions = ('export_batch_summary_action', )
    list_per_page = 100

    def export_batch_summary_action(self, request, queryset):
        headers = ['Sana', 'Mehmon', 'Fuqaroligi', 'Taklif qiluvchi tashkilot', 'Mas\'ul shaxs', 'Mehmonxona nomi',
                   'Mexmon kirgan kuni', 'Mexmon chiqqan kuni', 'Agent', 'Narxi(So\'mda)', 'Narxi($)',
                   'Yashagan kunlari', 'To\'lov statusi']
        rows = queryset.values_list('date', 'guest__guest_full_name', 'guest__citizenship__citizenship',
                                    'guest__personal_managers__company_offered__company_name',
                                    'guest__personal_managers__personal_manager', 'hotel_name',
                                    'guest_come_date', 'guest_back_date', 'employee__username', 'price', 'price_us',
                                    'hotel_days', 'payment_type')
        return export_to_excel_response('Hotel.xlsx', headers, rows)

    export_batch_summary_action.short_description = 'Export to excel'

    def get_days(self, obj):
        if obj.guest_come_date and not obj.guest_back_date:
            date = datetime.today().date() - obj.guest_come_date
            obj.hotel_days = str(date.days) + ' kun'
            obj.save()
            return date.days, 'kun'
        elif obj.guest_come_date and obj.guest_back_date:
            date = obj.guest_back_date - obj.guest_come_date
            obj.hotel_days = str(date.days) + ' kun'
            obj.save()
            return date.days, 'kun'

    get_days.short_description = 'Yashagan kunlari'


class OtherDocumentAdmin(admin.ModelAdmin):
    change_list_template = 'admin/total.html'
    list_display = ('date', 'guest', 'get_citizenship', 'get_company_offered', 'get_trip_goal', 'price',
                    'employee', 'payment_type')
    list_display_links = ('date', 'guest',)
    list_editable = ('payment_type',)
    search_fields = ('guest__guest_full_name', 'guest__personal_managers__company_offered__company_name')
    autocomplete_fields = ('guest',)
    list_filter = (  # ('guest_come_to_hotel_date', DateRangeFilter), ('guest_back_to_hotel_date', DateRangeFilter),
        'date', 'payment_type', 'employee')
    date_hierarchy = 'date'
    actions = ('export_batch_summary_action', )
    list_per_page = 100

    def export_batch_summary_action(self, request, queryset):
        headers = ['Sana', 'Mehmon', 'Fuqaroligi', 'Taklif qiluvchi tashkilot', 'Narxi(So\'mda)', 'Narxi($)',
                   'Agent', 'To\'lov statusi']
        rows = queryset.values_list('date', 'guest__guest_full_name', 'guest__citizenship__citizenship',
                                    'guest__personal_managers__company_offered__company_name', 'price',
                                    'price_us', 'employee__username', 'payment_type')
        return export_to_excel_response('ProcheDocs.xlsx', headers, rows)

    export_batch_summary_action.short_description = 'Export to excel'


class VisaControlAdmin(admin.ModelAdmin):
    change_list_template = 'admin/total.html'
    list_display = ('date', 'guest', 'employee', 'get_company_offered', 'get_citizenship', 'guest_come_date',
                    'guest_back_date', 'guest_living_address', 'guest_living_address_type', 'registration_date',
                    'visa_validate_date', 'license_date', 'possible_leave_date', 'get_personal_manager',
                    'guest_status', 'get_visa_days')
    list_display_links = ('date', 'guest',)
    search_fields = ('guest__guest_full_name', 'employee__username', 'guest_living_address',
                     'guest__personal_managers__personal_manager', 'guest__citizenship__citizenship',
                     'guest__personal_managers__company_offered__company_name')
    list_filter = ('date', 'guest_living_address_type', 'guest_status', 'employee')
    autocomplete_fields = ('guest',)
    date_hierarchy = 'date'
    actions = ('export_batch_summary_action', )
    list_per_page = 100

    def export_batch_summary_action(self, request, queryset):
        headers = ['Sana', 'Mehmon', 'Agent', 'Taklif qiluvchi tashkilot', 'Fuqaroligi', 'Mehmon keldi', 'Mehmon ketdi',
                   'Istiqomat qilayotgan manzil', 'Yashash joyi turi', 'Propiska muddati', 'Visa amal qilish muddati',
                   'Litsenziya muddati', 'Ehtimoliy ketish kuni', 'Buyurtmachi', 'Keldi\Ketdi', 'Kunlar soni']
        rows = queryset.values_list('date', 'guest__guest_full_name', 'employee__username',
                                    'guest__personal_managers__company_offered__company_name',
                                    'guest__citizenship__citizenship', 'guest_come_date', 'guest_back_date',
                                    'guest_living_address', 'guest_living_address_type', 'registration_date',
                                    'visa_validate_date', 'license_date', 'possible_leave_date',
                                    'guest__personal_managers__personal_manager', 'guest_status', 'visa_days')
        return export_to_excel_response('VisaControl.xlsx', headers, rows)

    export_batch_summary_action.short_description = 'Export to excel'

    def get_visa_days(self, obj):
        if obj.registration_date:
            date = obj.registration_date - datetime.today().date()
            obj.visa_days = str(date.days) + ' kun'
            obj.save()
            if date.days <= 20:
                obj.visa_days = str(date.days) + ' kun'
                obj.save()
                return format_html('<div style="background-color: #CC0000; color: #fff; padding: 5px;"> {}, kun </div>'
                                   .format(date.days))
            return date.days, 'kun'
        obj.visa_days = 'Propiska kiritilmagan'
        obj.save()
        return format_html('<div style="color: #CC0000">Propiska kiritilmagan')

    get_visa_days.short_description = 'Kunlar soni'


admin.site.register(GuestInfo, GuestInfoAdmin)
admin.site.register(PersonalManager, PersonalManagerAdmin)
admin.site.register(VisaCity, VisaCityAdmin)
admin.site.register(AirTicket, AirTicketAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(OtherDocument, OtherDocumentAdmin)
admin.site.register(VisaControl, VisaControlAdmin)

admin.site.site_header = 'Akfa Tour'
