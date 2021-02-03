from datetime import datetime

from django.contrib import admin
from django.utils.html import format_html

from .models import *


class CountryAdmin(admin.ModelAdmin):
    search_fields = ('country', )


class CarrierAdmin(admin.ModelAdmin):
    search_fields = ('name', )


class CitizenshipAdmin(admin.ModelAdmin):
    search_fields = ('citizenship', )


class CompanyOfferedAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'department')
    list_editable = ('department', )
    search_fields = ('company_name', 'department')


admin.site.register(Country, CountryAdmin)
admin.site.register(Carrier, CarrierAdmin)
admin.site.register(Citizenship, CitizenshipAdmin)
admin.site.register(Department)
admin.site.register(CompanyOffered, CompanyOfferedAdmin)
