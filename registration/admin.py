from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.db.models import Q, Count, Avg, Sum
from django.utils.html import format_html

from registration.models import *
from tour.models import VisaCity, AirTicket
from datetime import datetime


# from rangefilter.filter import DateRangeFilter


class ShengenVisaAdmin(admin.ModelAdmin):
    list_display = ('date', 'guest', 'get_company_offered', 'shengen_country', 'submitted_date', 'possible_leave_date')
    readonly_fields = ('get_company_offered',)
    search_fields = ('guest__guest_full_name',)
    list_filter = ('date',)
    autocomplete_fields = ('guest',)


class LicenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'guest', 'get_company_offered', 'license_submitted_date', 'license_over_date', 'get_days', 'status')
    # fields = list_display
    readonly_fields = ('get_company_offered', 'get_days')
    search_fields = ('guest__guest_full_name',)
    list_filter = ('date',)
    autocomplete_fields = ('guest',)
    # list_filter = (('date', DateRangeFilter), )

    def get_days(self, obj):
        if obj.license_over_date:
            date = obj.license_over_date - datetime.today().date()
            if date.days <= 20:
                return format_html('<div style="background-color: #CC0000; color: #fff; padding: 5px;"> {}, kun </div>'
                                   .format(date.days))
            return date.days, 'kun'
        return 'Tugash muddati kiritilmagan'

    get_days.short_description = 'Kunlar soni'


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('date', 'guest', 'get_passport', 'get_citizenship', 'get_company_offered', 'get_living_address',
                    'submitted_date', 'registration_date', 'visa_date', 'payment', 'get_personal_manager')
    # fields = list_display
    readonly_fields = ('get_passport', 'get_citizenship', 'get_company_offered', 'get_living_address',
                       'get_personal_manager')
    list_filter = ('date',)
    search_fields = ('guest__guest_full_name',)
    autocomplete_fields = ('guest',)


class PradVisaAdmin(admin.ModelAdmin):
    list_display = ('date', 'guest', 'get_passport', 'get_company_offered', 'submitted_address', 'submitted_date',
                    'taking_date', 'guarantee_letter', 'visa_over_date', 'payment')
    # fields = list_display
    readonly_fields = ('get_passport', 'get_company_offered')
    list_filter = ('date',)
    search_fields = ('guest__guest_full_name',)
    autocomplete_fields = ('guest',)


class ReportAdmin(admin.ModelAdmin):
    list_display = ('company_offered', 'get_ticket', 'get_visa_city', 'get_registration', 'get_prad_visa', 'get_licence',
                    'get_shengen', 'get_sum')
    search_fields = ('company_offered__company_name',)
    date_hierarchy = 'company_offered__personal_manager__guest__prad_visas__date'
    readonly_fields = ('get_visa_city', 'get_registration', 'get_prad_visa', 'get_licence', 'get_shengen', 'get_sum')

    def get_queryset(self, request):
        qs = super(ReportAdmin, self).get_queryset(request)
        # print('req', request.GET, 111111111111111)
        self.request = request
        path = request.get_full_path()
        url_params = path.split('?')
        req = url_params[-1]
        return qs

    def get_ticket(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        month = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__month')
        day = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__day')
        if year and not month and not day:
            company = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year)).count()
        elif year and month and not day:
            company = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=month)).count()
        elif year and month and day:
            company = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=month) & Q(date__day=month)).count()
        else:
            company = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered)).count()
        return company

    def get_visa_city(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        month = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__month')
        day = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__day')
        if year and not month and not day:
            company = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year)).count()
        elif year and month and not day:
            company = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=month)).count()
        elif year and month and day:
            company = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=month) & Q(date__day=month)).count()
        else:
            company = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered)).count()
        return company

    def get_registration(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        month = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__month')
        day = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__day')
        if year and not month and not day:
            company = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year)).count()
        elif year and month and not day:
            company = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=month)).count()
        elif year and month and day:
            company = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=month) & Q(date__day=month)).count()
        else:
            company = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered)).count()
        return company

    def get_prad_visa(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        month = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__month')
        day = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__day')
        if year and not month and not day:
            company = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year)).count()
        elif year and month and not day:
            company = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=month)).count()
        elif year and month and day:
            company = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=month) & Q(date__day=month)).count()
        else:
            company = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered)).count()
        return company

    def get_licence(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        month = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__month')
        day = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__day')
        if year and not month and not day:
            company = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year)).count()
        elif year and month and not day:
            company = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=month)).count()
        elif year and month and day:
            company = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=month) & Q(date__day=month)).count()
        else:
            company = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered)).count()
        return company

    def get_shengen(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        month = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__month')
        day = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__day')
        if year and not month and not day:
            company = ShengenVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year)).count()
        elif year and month and not day:
            company = ShengenVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=month)).count()
        elif year and month and day:
            company = ShengenVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=month) & Q(date__day=month)).count()
        else:
            company = ShengenVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered)).count()
        return company

    def get_sum(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        month = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__month')
        day = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__day')
        if year and not month and not day:
            visa_city = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                                Q(date__year=year))
            registration = Registration.objects.filter(
                Q(guest__personal_managers__company_offered=obj.company_offered) &
                Q(date__year=year))
            prad_visa = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                                Q(date__year=year))
            licence = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__year=year))
            shengen = ShengenVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                                 Q(date__year=year))
        elif year and month and not day:
            visa_city = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                                Q(date__year=year) & Q(date__month=month))
            registration = Registration.objects.filter(
                Q(guest__personal_managers__company_offered=obj.company_offered) &
                Q(date__year=year) & Q(date__month=month))
            prad_visa = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                                Q(date__year=year) & Q(date__month=month))
            licence = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__year=year) & Q(date__month=month))
            shengen = ShengenVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                                 Q(date__year=year) & Q(date__month=month))
        elif year and month and day:
            visa_city = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                                Q(date__year=year) & Q(date__month=month) & Q(date__day=month))
            registration = Registration.objects.filter(
                Q(guest__personal_managers__company_offered=obj.company_offered) &
                Q(date__year=year) & Q(date__month=month) & Q(date__day=month))
            prad_visa = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                                Q(date__year=year) & Q(date__month=month) & Q(date__day=month))
            licence = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__year=year) & Q(date__month=month) & Q(date__day=month))
            shengen = ShengenVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                                 Q(date__year=year) & Q(date__month=month) & Q(date__day=month))
        else:
            visa_city = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered))
            registration = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered))
            prad_visa = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered))
            licence = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered))
            shengen = ShengenVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered))

        sum = 0
        for item in visa_city:
            if item.price is not None:
                sum += item.price
        for item in registration:
            if item.price is not None:
                sum += item.price
        for item in prad_visa:
            if item.price is not None:
                sum += item.price
        for item in licence:
            if item.price is not None:
                sum += item.price
        for item in shengen:
            if item.price is not None:
                sum += item.price
        return '{:,}'.format(sum)

    # def has_add_permission(self, request):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    # def has_change_permission(self, request, obj=None):
    #     return False


class ChiefAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'company_offered', 'position', 'passport', 'zagran_visa', 'other_visa', 'image_tag', 'get_days')
    search_fields = ('name', 'company_offered__company_name', 'passport')
    list_display_links = list_display
    autocomplete_fields = ('company_offered', 'position')
    list_filter = ('zagran_visa', 'position')

    def get_days(self, obj):
        if obj.zagran_visa:
            date = obj.zagran_visa - datetime.today().date()
            if date.days <= 30:
                return format_html('<div style="background-color: #CC0000; color: #fff; padding: 5px;"> {}, kun </div>'
                                   .format(date.days))
            return date.days, 'kun'
        return 'Zagran visa kiritilmagan'

    get_days.short_description = 'Kunlar soni'


class PositionAdmin(admin.ModelAdmin):
    list_display = ('date', 'position')
    search_fields = ('position',)


admin.site.register(ShengenVisa, ShengenVisaAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(PradVisa, PradVisaAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Chief, ChiefAdmin)
admin.site.register(Position, PositionAdmin)
from django.utils.html import format_html

logo_url = 'http://citizentravel.uz/wp-content/themes/citizentravel/img/logo.svg'
admin.site.site_header = format_html("<img src={url} height=50 width=180>", url=logo_url)
