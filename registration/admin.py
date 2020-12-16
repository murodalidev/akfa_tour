from django.contrib import admin
from registration.models import *


class ShengenVisaAdmin(admin.ModelAdmin):
    list_display = ('guest_full_name', 'company_offered', 'shengen_country', 'submitted_date', 'possible_leave_date')


class LicenseAdmin(admin.ModelAdmin):
    list_display = ('guest_full_name', 'company_offered', 'license_submitted_date', 'license_over_date', 'status')


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('guest_full_name', 'passport_id', 'citizenship', 'company_offered', 'guest_living_address',
                    'submitted_date', 'registration_date', 'visa_date', 'payment', 'personal_manager')


class PradVisaAdmin(admin.ModelAdmin):
    list_display = ('guest_full_name', 'passport_id', 'company_offered', 'submitted_address', 'submitted_date',
                    'taking_date', 'guarantee_letter', 'visa_over_date', 'payment')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('company_offered', 'visa_city', 'registration', 'prad_visa', 'shengen_visa', 'total')


admin.site.register(ShengenVisa, ShengenVisaAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(PradVisa, PradVisaAdmin)
admin.site.register(Report, ReportAdmin)
