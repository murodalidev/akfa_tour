from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.db.models.signals import post_delete, post_save
from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler
from database.models import CompanyOffered
from tour.models import GuestInfo, PersonalManager, VisaControl

payment_type = (
    ('transfer', 'Perechesleniya'),
    ('transfer_ok', 'Pereches-OK'),
    ('payed', 'To\'landi'),
    ('not_payed', 'To\'lanmadi'),
)


class ShengenVisa(ChangeloggableMixin, models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE, verbose_name='FISH')
    shengen_country = models.CharField(max_length=100, verbose_name='Shengen davlati', null=True, blank=True)
    submitted_date = models.DateField(null=True, blank=True, verbose_name='Topshirilgan kun')
    possible_leave_date = models.DateField(null=True, blank=True, verbose_name='Ehtimoliy chiqish kuni')
    price = models.FloatField(null=True, blank=True, verbose_name='Narxi', default=400000.0)
    payment_type = models.CharField(choices=payment_type, default='transfer', max_length=50, verbose_name='To\'lov statusi')

    def get_company_offered(self):
        company_offered = PersonalManager.objects.get(guest_id=self.guest_id)
        return company_offered.company_offered
    get_company_offered.short_description = 'Taklif qiluvchi tashkilot'

    class Meta:
        verbose_name_plural = "1. Shengen Visa"


post_save.connect(journal_save_handler, sender=ShengenVisa)
post_delete.connect(journal_delete_handler, sender=ShengenVisa)


class License(ChangeloggableMixin, models.Model):
    status = (
        ('jarayonda', 'jarayonda'),
        ('kerakmas', 'kerakmas'),
        ('ketti', 'ketti'),
        ('olingan', 'olingan'),
        ('olish_kerak', 'olish_kerak'),
        ('otmen', 'otmen'),
        ('yangi', 'yangi'),
    )
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE, verbose_name='FISH', related_name='licenses')
    license_submitted_date = models.DateField(null=True, blank=True, verbose_name='Litsensizyaga topshirilgan kun')
    license_over_date = models.DateField(null=True, blank=True, verbose_name='Litsenziya tugash muddati')
    status = models.CharField(choices=status, max_length=50, verbose_name='Holati', default='jarayonda')
    price = models.FloatField(null=True, blank=True, verbose_name='Narxi', default=600000.0)
    payment_type = models.CharField(choices=payment_type, default='transfer', max_length=50, verbose_name='To\'lov statusi')

    def get_company_offered(self):
        company_offered = PersonalManager.objects.get(guest_id=self.guest_id)
        return company_offered.company_offered
    get_company_offered.short_description = 'Taklif qiluvchi tashkilot'

    class Meta:
        verbose_name_plural = "2. Licence"


post_save.connect(journal_save_handler, sender=License)
post_delete.connect(journal_delete_handler, sender=License)


class Registration(ChangeloggableMixin, models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE, verbose_name='FISH', related_name='regs')
    submitted_date = models.DateField(null=True, blank=True, verbose_name='Topshirilgan sana')
    registration_date = models.DateField(null=True, blank=True, verbose_name='Propiska muddati')
    visa_date = models.DateField(null=True, blank=True, verbose_name='Visa muddati')
    payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.FloatField(null=True, blank=True, verbose_name='Narxi', default=300000.0)
    payment_type = models.CharField(choices=payment_type, default='transfer', max_length=50, verbose_name='To\'lov statusi')

    def get_passport(self):
        return self.guest.passport_id
    get_passport.short_description = 'Passport'

    def get_citizenship(self):
        return self.guest.citizenship
    get_citizenship.short_description = 'Fuqaroligi'

    def get_company_offered(self):
        company_offered = PersonalManager.objects.get(guest_id=self.guest_id)
        return company_offered.company_offered
    get_company_offered.short_description = 'Taklif qiluvchi tashkilot'

    def get_living_address(self):
        living_address = VisaControl.objects.get(guest_id=self.guest_id)
        return living_address.guest_living_address
    get_living_address.short_description = 'Toliq manzili'

    def get_personal_manager(self):
        personal_manager = PersonalManager.objects.get(guest_id=self.guest_id)
        return personal_manager.personal_manager
    get_personal_manager.short_description = 'Mas\'ul shaxs'

    class Meta:
        verbose_name_plural = "3. Registration"


post_save.connect(journal_save_handler, sender=Registration)
post_delete.connect(journal_delete_handler, sender=Registration)


class PradVisa(ChangeloggableMixin, models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE, verbose_name='FISH', related_name='prad_visas')
    submitted_address = models.DateField(null=True, blank=True, verbose_name='Topshirilgan manzil')
    submitted_date = models.DateField(null=True, blank=True, verbose_name='Topshirilgan sana')
    taking_date = models.DateField(null=True, blank=True, verbose_name='Olish sana')
    guarantee_letter = models.CharField(null=True, blank=True, max_length=100, verbose_name='Гарантийное письмо')
    visa_over_date = models.DateField(null=True, blank=True, verbose_name='Visa tugash muddati')
    price = models.FloatField(null=True, blank=True, verbose_name='Narxi', default=300000.0)
    payment_type = models.CharField(choices=payment_type, default='transfer', max_length=50, verbose_name='To\'lov statusi')
    payment = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, verbose_name='Kassa to\'lovi')

    def __str__(self):
        return f'{self.guest} to {self.get_company_offered()}'

    def get_passport(self):
        return self.guest.passport_id
    get_passport.short_description = 'Passport'

    def get_company_offered(self):
        company_offered = PersonalManager.objects.get(guest_id=self.guest_id)
        return company_offered.company_offered
    get_company_offered.short_description = 'Taklif qiluvchi tashkilot'

    class Meta:
        verbose_name_plural = "4. PradVisa"


post_save.connect(journal_save_handler, sender=PradVisa)
post_delete.connect(journal_delete_handler, sender=PradVisa)


class Report(ChangeloggableMixin, models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE, verbose_name='Tashkilot nomi',
                                        null=True, blank=True)

    def __str__(self):
        return f'{self.company_offered}'

    class Meta:
        verbose_name_plural = "5. Reports"


post_save.connect(journal_save_handler, sender=Report)
post_delete.connect(journal_delete_handler, sender=Report)


class Position(ChangeloggableMixin, models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    position = models.CharField(max_length=100, verbose_name='Pozitsiya')

    def __str__(self):
        return f'{self.position}'

    class Meta:
        verbose_name_plural = "7. Positions"


post_save.connect(journal_save_handler, sender=Position)
post_delete.connect(journal_delete_handler, sender=Position)


class Chief(ChangeloggableMixin, models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    name = models.CharField(max_length=100, verbose_name='FISH')
    company_offered = models.ForeignKey(CompanyOffered, verbose_name='Tashkilot', on_delete=models.CASCADE)
    position = models.ForeignKey(Position, verbose_name='Pazitsiyasi', on_delete=models.CASCADE)
    passport = models.CharField(max_length=9, verbose_name='Passport', null=True, blank=True)
    zagran_visa = models.DateField(verbose_name='Zagran passport sana', null=True, blank=True)
    other_visa = models.DateField(verbose_name='Bohsqa visa', null=True, blank=True)
    visa_img = models.ImageField(verbose_name='visa rasmi', null=True, blank=True)

    def image_tag(self):
        if self.visa_img:
            return mark_safe(f'<a href="{self.visa_img.url}"><img src="{self.visa_img.url}" style="height:60px;"/></a>')
        else:
            return 'Rasm yuklanmagan'

    image_tag.short_description = 'visa rasmi'

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name_plural = "6. Chiefs"


post_save.connect(journal_save_handler, sender=Chief)
post_delete.connect(journal_delete_handler, sender=Chief)
