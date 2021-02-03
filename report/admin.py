from database.models import Department
from registration.models import Registration
from report.models import *
from tour.models import AirTicket, Hotel, OtherDocument
from report.service_admin import *


class TotalReportAdmin(admin.ModelAdmin):
    change_list_template = 'admin/total-report.html'
    list_display = ('company_offered', 'get_ticket', 'get_hotel', 'get_visa', 'get_reg')
    date_hierarchy = 'company_offered__personal_manager__guest__airtickets__date'
    # list_filter = ('company_offered__department__name', )

    def has_add_permission(self, request):
        return False

    def changelist_view(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}
        extra_context.update({
            'departments': Department.objects.all()
        })
        return super(TotalReportAdmin, self).changelist_view(request, extra_context)

    def get_queryset(self, request):
        qs = super(TotalReportAdmin, self).get_queryset(request)
        self.request = request
        return qs

    def get_ticket(self, obj):
        ticket = AirTicket.objects.filter(guest__personal_managers__company_offered=obj.company_offered)
        t = 0
        for i in ticket:
            if i.price is not None:
                t += i.price

        return t

    def get_hotel(self, obj):
        hotel = Hotel.objects.filter(guest__personal_managers__company_offered=obj.company_offered)
        t = 0
        for i in hotel:
            if i.price is not None:
                t += i.price
        return t

    def get_visa(self, obj):
        other = OtherDocument.objects.filter(guest__personal_managers__company_offered=obj.company_offered)
        t = 0
        for i in other:
            if i.price is not None:
                t += i.price
        return t

    def get_reg(self, obj):
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
                                                  Q(date__year=year) & Q(date__month=month) & Q(
                date__day=month)).count()
        else:
            company = Registration.objects.filter(
                Q(guest__personal_managers__company_offered=obj.company_offered)).count()
        sum = 0
        if company > 0:
            sum += company * 300000
        return sum


class AirTicketReportAdmin(admin.ModelAdmin):
    change_list_template = 'admin/ignore_month.html'
    list_display = ('company_offered', 'get_jan', 'get_feb', 'get_march', 'get_apr', 'get_may', 'get_jun', 'get_jul',
                    'get_aug', 'get_sep', 'get_oct', 'get_nov', 'get_dec', 'get_total', 'get_per')
    list_filter = ('company_offered__department', 'company_offered__personal_manager__guest__airtickets__citizen')
    date_hierarchy = 'company_offered__personal_manager__guest__airtickets__date'
    search_fields = ('company_offered__company_name',)

    def get_jan(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__year=year) & Q(date__month=1))
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__month=1))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_feb(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__year=year) & Q(date__month=2))
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__month=2))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_march(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__year=year) & Q(date__month=3))
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__month=3))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_apr(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__year=year) & Q(date__month=4))
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__month=4))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_may(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__year=year) & Q(date__month=5))
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__month=5))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_jun(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__year=year) & Q(date__month=6))
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__month=6))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_jul(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__year=year) & Q(date__month=7))
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__month=7))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_aug(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__year=year) & Q(date__month=8))
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__month=8))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_sep(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__year=year) & Q(date__month=9))
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__month=9))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_oct(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__year=year) & Q(date__month=10))
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__month=10))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_nov(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__year=year) & Q(date__month=11))
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__month=11))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_dec(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__year=year) & Q(date__month=12))
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__month=12))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_total(self, obj):
        total = self.get_jan(obj) + self.get_feb(obj) + self.get_march(obj) + self.get_apr(obj) + self.get_may(
            obj) + self.get_jun(obj) + self.get_jul(obj) + self.get_aug(obj) + self.get_sep(obj) + self.get_oct(
            obj) + self.get_nov(obj) + self.get_dec(obj)
        obj.total = total
        obj.save()
        total_cost = 0
        print(obj.company_offered)
        return total

    def get_queryset(self, request):
        qs = super(AirTicketReportAdmin, self).get_queryset(request)
        self.request = request
        self.qs = qs
        return qs

    def get_per(self, obj):
        t = 0
        p = 0
        for i in self.qs:
            t += i.total
            if t != 0:
                p = (self.get_total(obj) / t) * 100
        return str(p)[:5] + '   %'


class GuestReportAdmin(admin.ModelAdmin):
    change_list_template = 'admin/ignore_month.html'
    list_display = ('company_offered', 'get_jan', 'get_feb', 'get_march', 'get_apr', 'get_may', 'get_jun', 'get_jul',
                    'get_aug', 'get_sep', 'get_oct', 'get_nov', 'get_dec', 'get_total', 'get_per')
    list_filter = ('company_offered__department', 'company_offered__personal_manager__guest__airtickets__citizen')
    date_hierarchy = 'company_offered__personal_manager__guest__airtickets__date'
    search_fields = ('company_offered__company_name', )

    def get_queryset(self, request):
        qs = super(GuestReportAdmin, self).get_queryset(request)
        self.request = request
        self.qs = qs
        return qs

    def get_jan(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=1)).count()

        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) & Q(date__month=1)).count()
        return count

    def get_feb(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=2)).count()
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) & Q(date__month=2)).count()
        return count

    def get_march(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=3)).count()
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) & Q(date__month=3)).count()
        return count

    def get_apr(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=4)).count()
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) & Q(date__month=4)).count()
        return count

    def get_may(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=5)).count()
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) & Q(date__month=5)).count()
        return count

    def get_jun(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=6)).count()
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) & Q(date__month=6)).count()
        return count

    def get_jul(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=7)).count()
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) & Q(date__month=7)).count()
        return count

    def get_aug(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=8)).count()
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) & Q(date__month=8)).count()
        return count

    def get_sep(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=9)).count()
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) & Q(date__month=9)).count()
        return count

    def get_oct(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=10)).count()
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) & Q(date__month=10)).count()
        return count

    def get_nov(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=11)).count()
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                             Q(date__month=11)).count()
        return count

    def get_dec(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
        if year:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=12)).count()
        else:
            count = AirTicket.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) & Q(date__month=12)).count()
        return count

    def get_total(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__airtickets__date__year')
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

        i = self.get_jan(obj) + self.get_feb(obj) + self.get_march(obj) + self.get_apr(obj) + self.get_may(
            obj) + self.get_jun(obj) + self.get_jul(obj) + self.get_aug(obj) + self.get_sep(obj) + self.get_oct(
            obj) + self.get_nov(obj) + self.get_dec(obj)
        obj.total = i
        obj.save()
        return i

    def get_per(self, obj):
        t = 0
        p = 0
        for i in self.qs:
            t += i.total
            if t != 0:
                p = (self.get_total(obj) / t) * 100
        return str(p)[:5] + '   %'


class HotelReportAdmin(admin.ModelAdmin):
    change_list_template = 'admin/ignore_month.html'
    list_display = ('company_offered', 'get_jan', 'get_feb', 'get_march', 'get_apr', 'get_may', 'get_jun', 'get_jul',
                    'get_aug', 'get_sep', 'get_oct', 'get_nov', 'get_dec', 'get_total', 'get_per')
    list_filter = ('company_offered__department', 'company_offered__personal_manager__guest__hotels__payment_type')
    date_hierarchy = 'company_offered__personal_manager__guest__hotels__date'
    search_fields = ('company_offered__company_name',)

    def get_queryset(self, request):
        qs = super(HotelReportAdmin, self).get_queryset(request)
        self.request = request
        self.qs = qs
        return qs

    def get_jan(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__hotels__date__year')
        # print(year)
        if year:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=1))

        else:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=1))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_feb(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__hotels__date__year')
        if year:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=2))

        else:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=2))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_march(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__hotels__date__year')
        if year:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=3))

        else:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=3))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_apr(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__hotels__date__year')
        if year:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=4))

        else:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=4))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_may(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__hotels__date__year')
        if year:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=5))

        else:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=5))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_jun(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__hotels__date__year')
        if year:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=6))

        else:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=6))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_jul(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__hotels__date__year')
        if year:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=7))

        else:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=7))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_aug(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__hotels__date__year')
        if year:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=8))

        else:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=8))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_sep(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__hotels__date__year')
        if year:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=9))

        else:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=9))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_oct(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__hotels__date__year')
        if year:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=10))

        else:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=10))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_nov(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__hotels__date__year')
        if year:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=11))

        else:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=11))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_dec(self, obj):
        year = self.request.GET.get('company_offered__personal_manager__guest__hotels__date__year')
        if year:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                              Q(date__year=year) & Q(date__month=12))

        else:
            count = Hotel.objects.filter(Q(guest__personal_managers__company_offered=obj.company_offered) &
                                         Q(date__month=12))
        t = 0.0
        for i in count:
            if i.price is not None:
                t += float(i.price)
        return t

    def get_total(self, obj):
        i = self.get_jan(obj) + self.get_feb(obj) + self.get_march(obj) + self.get_apr(obj) + self.get_may(
            obj) + self.get_jun(obj) + self.get_jul(obj) + self.get_aug(obj) + self.get_sep(obj) + self.get_oct(
            obj) + self.get_nov(obj) + self.get_dec(obj)
        # print(i)
        obj.total = i
        obj.save()
        return i

    def get_per(self, obj):
        t = 0
        p = 0
        for i in self.qs:
            t += i.total
            if t != 0:
                p = (self.get_total(obj) / t) * 100
        return str(p)[:5] + '   %'


admin.site.register(AirTicketReport, AirTicketReportAdmin)
admin.site.register(GuestReport, GuestReportAdmin)
admin.site.register(HotelReport, HotelReportAdmin)
admin.site.register(TotalReport, TotalReportAdmin)
