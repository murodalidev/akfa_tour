from django.db import models
from database.models import CompanyOffered


class ShengenVisa(models.Model):
    guest_full_name = models.CharField(max_length=100, verbose_name='FISH', null=True, blank=True)
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE, verbose_name='Tashkilot nomi',
                                        null=True, blank=True)
    shengen_country = models.CharField(max_length=100, verbose_name='Shengen davlati', null=True, blank=True)
    submitted_date = models.DateField(null=True, blank=True, verbose_name='Topshirilgan kun')
    possible_leave_date = models.DateField(null=True, blank=True, verbose_name='Ehtimoliy chiqish kuni')


class License(models.Model):
    status = (
        ('jarayonda', 'jarayonda'),
        ('kerakmas', 'kerakmas'),
        ('ketti', 'ketti'),
        ('olingan', 'olingan'),
        ('olish_kerak', 'olish_kerak'),
        ('otmen', 'otmen'),
        ('yangi', 'yangi'),
    )
    guest_full_name = models.CharField(max_length=100, verbose_name='FISH', null=True, blank=True)
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE, verbose_name='Tashkilot nomi',
                                        null=True, blank=True)
    license_submitted_date = models.DateField(null=True, blank=True, verbose_name='Litsensizyaga topshirilgan kun')
    license_over_date = models.DateField(null=True, blank=True, verbose_name='Litsenziya tugash muddati')
    status = models.CharField(choices=status, max_length=50, verbose_name='Holati', default='jarayonda')


class Registration(models.Model):
    guest_full_name = models.CharField(max_length=100, verbose_name='FISH', null=True, blank=True)
    passport_id = models.CharField(max_length=15, verbose_name='Passport', null=True, blank=True)
    citizenship = models.CharField(max_length=100, verbose_name='Fuqaroligi', null=True, blank=True)
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE, verbose_name='Tashkilot nomi',
                                        null=True, blank=True)
    guest_living_address = models.CharField(null=True, blank=True, max_length=255, verbose_name='Toliq manzili')
    submitted_date = models.DateField(null=True, blank=True, verbose_name='Topshirilgan sana')
    registration_date = models.DateField(null=True, blank=True, verbose_name='Propiska muddati')
    visa_date = models.DateField(null=True, blank=True, verbose_name='Visa muddati')
    payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    personal_manager = models.CharField(max_length=255, null=True, blank=True, verbose_name='Mas\'ul shaxs')


class PradVisa(models.Model):
    guest_full_name = models.CharField(max_length=100, verbose_name='FISH', null=True, blank=True)
    passport_id = models.CharField(max_length=15, verbose_name='Passport', null=True, blank=True)
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE, verbose_name='Tashkilot nomi',
                                        null=True, blank=True)
    submitted_address = models.DateField(null=True, blank=True, verbose_name='Topshirilgan manzil')
    submitted_date = models.DateField(null=True, blank=True, verbose_name='Topshirilgan sana')
    taking_date = models.DateField(null=True, blank=True, verbose_name='Olish sana')
    guarantee_letter = models.CharField(null=True, blank=True, max_length=100, verbose_name='Гарантийное письмо')
    visa_over_date = models.DateField(null=True, blank=True, verbose_name='Visa tugash muddati')
    payment = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, verbose_name='Kassa to\'lovi')


class Report(models.Model):
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE, verbose_name='Tashkilot nomi',
                                        null=True, blank=True)
    visa_city = models.IntegerField(verbose_name='Visa City', null=True, blank=True, default=0)
    registration = models.IntegerField(verbose_name='Registratsiya', null=True, blank=True, default=0)
    prad_visa = models.IntegerField(verbose_name='Prad/Visa', null=True, blank=True, default=0)
    shengen_visa = models.IntegerField(verbose_name='Shengen Visa', null=True, blank=True, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Summa', null=True, blank=True, default=0)