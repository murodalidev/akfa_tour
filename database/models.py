from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.utils.timezone import now
from django.db.models.signals import post_delete, post_save
from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler


class Country(ChangeloggableMixin, models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    country = models.CharField(max_length=100, verbose_name='Davlat')
    created_date = models.DateTimeField(auto_now_add=True, editable=True, verbose_name='Tizimga iritilgan sana')

    def __str__(self):
        return self.country

    class Meta:
        ordering = ('country',)
        verbose_name_plural = "1. Country"


post_save.connect(journal_save_handler, sender=Country)
post_delete.connect(journal_delete_handler, sender=Country)


class Carrier(ChangeloggableMixin, models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    name = models.CharField(max_length=100, verbose_name='Aviatashuvchi')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Tizimga iritilgan sana')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = '2. Carrier'


post_save.connect(journal_save_handler, sender=Carrier)
post_delete.connect(journal_delete_handler, sender=Carrier)


class Citizenship(ChangeloggableMixin, models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    citizenship = models.CharField(max_length=50, verbose_name='Fuqaroligi')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Tizimga iritilgan sana')

    def __str__(self):
        return self.citizenship

    class Meta:
        ordering = ('citizenship',)
        verbose_name_plural = '3. Citizenship'


post_save.connect(journal_save_handler, sender=Citizenship)
post_delete.connect(journal_delete_handler, sender=Citizenship)


class Department(ChangeloggableMixin, models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '4. Department'

    def get_data(self, model, year):
        offered_companies = CompanyOffered.objects.filter(department=self).values_list('id', flat=True)
        data = []
        items = model.objects.filter(date__year=year, guest__personal_managers__company_offered__in=offered_companies)
        for month in range(1, 13):
            total = items.filter(date__month=month).aggregate(total_price=Sum('price')).get('total_price') or 0
            data.append(total)
        return data

    def get_report_types(self, year):
        from tour.models import AirTicket, Hotel, VisaCity
        from registration.models import Registration

        return [{
            'title': 'Air tickets',
            'data': self.get_data(model=AirTicket, year=year)
        }, {
            'title': 'Hotels',
            'data': self.get_data(model=Hotel, year=year)
        }, {
            'title': 'Visa',
            'data': self.get_data(model=VisaCity, year=year)
        }, {
            'title': 'Registration',
            'data': self.get_data(model=Registration, year=year)
        }]


post_save.connect(journal_save_handler, sender=Department)
post_delete.connect(journal_delete_handler, sender=Department)


class CompanyOffered(ChangeloggableMixin, models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    company_name = models.CharField(max_length=255, verbose_name='Taklif qiluvchi tashkilot nomi')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Tizimga iritilgan sana')

    def __str__(self):
        return self.company_name

    class Meta:
        ordering = ('company_name',)
        verbose_name_plural = '5. CompanyOffered'


post_save.connect(journal_save_handler, sender=CompanyOffered)
post_delete.connect(journal_delete_handler, sender=CompanyOffered)
