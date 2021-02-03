from django.contrib import admin
from django.db.models import Q
from report.models import ServiceReportMid, ServiceReportPradVisa, ServiceReportLicence, ServiceReportReg
from tour.models import VisaCity
from registration.models import PradVisa, Registration, License


class ServiceReportMidAdmin(admin.ModelAdmin):
    change_list_template = 'admin/ignore_month.html'
    list_display = ('company_offered', 'get_jan', 'get_feb', 'get_march', 'get_apr', 'get_may', 'get_jun', 'get_jul',
                    'get_aug', 'get_sep', 'get_oct', 'get_nov', 'get_dec', 'get_total')
    list_filter = ('company_offered__department', )
    search_fields = ('company_offered__company_name',)
    date_hierarchy = 'company_offered__personal_manager__guest__mid__date'

    def get_queryset(self, request):
        qs = super(ServiceReportMidAdmin, self).get_queryset(request)
        self.request = request
        self.qs = qs
        return qs

    def get_jan(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__mid__date__year')
        # print(year)
        if year:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=1)).count()

        else:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=1)).count()
        return count

    def get_feb(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__mid__date__year')
        if year:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=2)).count()

        else:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=2)).count()
        return count

    def get_march(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__mid__date__year')
        if year:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=3)).count()

        else:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=3)).count()
        return count

    def get_apr(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__mid__date__year')
        if year:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=4)).count()

        else:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=4)).count()
        return count

    def get_may(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__mid__date__year')
        if year:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=5)).count()

        else:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=5)).count()
        return count

    def get_jun(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__mid__date__year')
        if year:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=6)).count()

        else:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=6)).count()
        return count

    def get_jul(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__mid__date__year')
        if year:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=7)).count()

        else:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=7)).count()
        return count

    def get_aug(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__hotels__date__year')
        if year:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=8)).count()

        else:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=8)).count()
        return count

    def get_sep(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__mid__date__year')
        if year:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=9)).count()

        else:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=9)).count()
        return count

    def get_oct(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__mid__date__year')
        if year:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=10)).count()

        else:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=10)).count()
        return count

    def get_nov(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__mid__date__year')
        if year:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=11)).count()

        else:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=11)).count()
        return count

    def get_dec(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__mid__date__year')
        if year:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=12)).count()

        else:
            count = VisaCity.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=12)).count()
        return count

    def get_total(self, obj):
        i = self.get_jan(obj) + self.get_feb(obj) + self.get_march(obj) + self.get_apr(obj) + self.get_may(
            obj) + self.get_jun(obj) + self.get_jul(obj) + self.get_aug(obj) + self.get_sep(obj) + self.get_oct(
            obj) + self.get_nov(obj) + self.get_dec(obj)
        obj.total = i
        obj.save()
        return i


class ServiceReportPradVisaAdmin(admin.ModelAdmin):
    change_list_template = 'admin/ignore_month.html'
    list_display = ('company_offered', 'get_jan', 'get_feb', 'get_march', 'get_apr', 'get_may', 'get_jun', 'get_jul',
                    'get_aug', 'get_sep', 'get_oct', 'get_nov', 'get_dec', 'get_total')
    search_fields = ('company_offered__company_name',)
    date_hierarchy = 'company_offered__personal_manager__guest__prad_visas__date'
    list_filter = ('company_offered__department', date_hierarchy)

    def get_queryset(self, request):
        qs = super(ServiceReportPradVisaAdmin, self).get_queryset(request)
        self.request = request
        self.qs = qs
        return qs

    def get_jan(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        if year:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=1)).count()

        else:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=1)).count()
        print(PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                          Q(date__year=year) & Q(date__month=1)))

        return count

    def get_feb(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        if year:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=2)).count()

        else:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=2)).count()
        return count

    def get_march(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        if year:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=3)).count()

        else:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=3)).count()
        return count

    def get_apr(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        if year:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=4)).count()

        else:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=4)).count()
        return count

    def get_may(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        if year:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=5)).count()

        else:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=5)).count()
        return count

    def get_jun(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        if year:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=6)).count()

        else:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=6)).count()
        return count

    def get_jul(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        if year:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=7)).count()

        else:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=7)).count()
        return count

    def get_aug(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        if year:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=8)).count()

        else:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=8)).count()
        return count

    def get_sep(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        if year:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=9)).count()

        else:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=9)).count()
        return count

    def get_oct(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        if year:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=10)).count()

        else:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=10)).count()
        return count

    def get_nov(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        if year:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=11)).count()

        else:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=11)).count()
        return count

    def get_dec(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__prad_visas__date__year')
        if year:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=12)).count()

        else:
            count = PradVisa.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=12)).count()
        return count

    def get_total(self, obj):
        i = self.get_jan(obj) + self.get_feb(obj) + self.get_march(obj) + self.get_apr(obj) + self.get_may(
            obj) + self.get_jun(obj) + self.get_jul(obj) + self.get_aug(obj) + self.get_sep(obj) + self.get_oct(
            obj) + self.get_nov(obj) + self.get_dec(obj)
        obj.total = i
        obj.save()
        return i


class ServiceReportRegAdmin(admin.ModelAdmin):
    change_list_template = 'admin/ignore_month.html'
    list_display = ('company_offered', 'get_jan', 'get_feb', 'get_march', 'get_apr', 'get_may', 'get_jun', 'get_jul',
                    'get_aug', 'get_sep', 'get_oct', 'get_nov', 'get_dec', 'get_total')
    search_fields = ('company_offered__company_name',)
    date_hierarchy = 'company_offered__personal_manager__guest__regs__date'
    list_filter = ('company_offered__department', date_hierarchy)

    def get_queryset(self, request):
        qs = super(ServiceReportRegAdmin, self).get_queryset(request)
        self.request = request
        self.qs = qs
        return qs

    def get_jan(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__regs__date')
        # print(year)
        if year:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=1)).count()

        else:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=1)).count()

        return count

    def get_feb(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__regs__date')
        if year:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=2)).count()

        else:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=2)).count()
        return count

    def get_march(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__regs__date')
        if year:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=3)).count()

        else:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=3)).count()
        return count

    def get_apr(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__regs__date')
        if year:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=4)).count()

        else:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=4)).count()
        return count

    def get_may(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__regs__date')
        if year:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=5)).count()

        else:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=5)).count()
        return count

    def get_jun(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__regs__date')
        if year:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=6)).count()

        else:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=6)).count()
        return count

    def get_jul(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__regs__date')
        if year:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=7)).count()

        else:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=7)).count()
        return count

    def get_aug(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__regs__date')
        if year:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=8)).count()

        else:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=8)).count()
        return count

    def get_sep(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__regs__date')
        if year:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=9)).count()

        else:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=9)).count()
        return count

    def get_oct(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__regs__date')
        if year:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=10)).count()

        else:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=10)).count()
        return count

    def get_nov(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__regs__date')
        if year:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=11)).count()

        else:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=11)).count()
        return count

    def get_dec(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__regs__date')
        if year:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=12)).count()

        else:
            count = Registration.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=12)).count()
        return count

    def get_total(self, obj):
        i = self.get_jan(obj) + self.get_feb(obj) + self.get_march(obj) + self.get_apr(obj) + self.get_may(
            obj) + self.get_jun(obj) + self.get_jul(obj) + self.get_aug(obj) + self.get_sep(obj) + self.get_oct(
            obj) + self.get_nov(obj) + self.get_dec(obj)
        obj.total = i
        obj.save()
        return i


class ServiceReportLicenceAdmin(admin.ModelAdmin):
    change_list_template = 'admin/ignore_month.html'
    list_display = ('company_offered', 'get_jan', 'get_feb', 'get_march', 'get_apr', 'get_may', 'get_jun', 'get_jul',
                    'get_aug', 'get_sep', 'get_oct', 'get_nov', 'get_dec', 'get_total')
    search_fields = ('company_offered__company_name',)
    date_hierarchy = 'company_offered__personal_manager__guest__licenses__date'
    list_filter = ('company_offered__department', date_hierarchy)

    def get_queryset(self, request):
        qs = super(ServiceReportLicenceAdmin, self).get_queryset(request)
        self.request = request
        self.qs = qs
        return qs

    def get_jan(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__licenses__date__year')
        if year:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=1)).count()

        else:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=1)).count()

        return count

    def get_feb(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__licenses__date__year')
        if year:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=2)).count()

        else:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=2)).count()
        return count

    def get_march(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__licenses__date__year')
        if year:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=3)).count()

        else:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=3)).count()
        return count

    def get_apr(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__licenses__date__year')
        if year:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=4)).count()

        else:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=4)).count()
        return count

    def get_may(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__licenses__date__year')
        if year:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=5)).count()

        else:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=5)).count()
        return count

    def get_jun(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__licenses__date__year')
        if year:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=6)).count()

        else:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=6)).count()
        return count

    def get_jul(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__licenses__date__year')
        if year:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=7)).count()

        else:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=7)).count()
        return count

    def get_aug(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__licenses__date__year')
        if year:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=8)).count()

        else:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=8)).count()
        return count

    def get_sep(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__licenses__date__year')
        if year:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=9)).count()

        else:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=9)).count()
        return count

    def get_oct(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__licenses__date__year')
        if year:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=10)).count()

        else:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=10)).count()
        return count

    def get_nov(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__licenses__date__year')
        if year:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=11)).count()

        else:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=11)).count()
        return count

    def get_dec(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__licenses__date__year')
        if year:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=12)).count()

        else:
            count = License.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=12)).count()
        return count

    def get_total(self, obj):
        i = self.get_jan(obj) + self.get_feb(obj) + self.get_march(obj) + self.get_apr(obj) + self.get_may(
            obj) + self.get_jun(obj) + self.get_jul(obj) + self.get_aug(obj) + self.get_sep(obj) + self.get_oct(
            obj) + self.get_nov(obj) + self.get_dec(obj)
        obj.total = i
        obj.save()
        return i


admin.site.register(ServiceReportMid, ServiceReportMidAdmin)
admin.site.register(ServiceReportPradVisa, ServiceReportPradVisaAdmin)
admin.site.register(ServiceReportReg, ServiceReportRegAdmin)
admin.site.register(ServiceReportLicence, ServiceReportLicenceAdmin)
# admin.site.register(ServiceReportResident)