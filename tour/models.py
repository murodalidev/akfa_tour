from datetime import datetime
from django.db.models.signals import post_delete, post_save
from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler

from django.contrib.auth.models import User
from database.models import *

payment = (
    ('transfer', 'Perechesleniya'),
    ('transfer_ok', 'Pereches-OK'),
    ('payed', 'To\'landi'),
    ('not_payed', 'To\'lanmadi'),
)


class GuestInfo(ChangeloggableMixin, models.Model):
    guest_full_name = models.CharField(max_length=100, verbose_name='FISH')
    passport_id = models.CharField(max_length=15, verbose_name='Passport')
    citizenship = models.ForeignKey(Citizenship, on_delete=models.CASCADE, verbose_name='Fuqaroligi')
    foreign_company = models.CharField(max_length=100, verbose_name='Xorijiy tashkilot nomi')
    created_date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')

    def __str__(self):
        return self.guest_full_name

    class Meta:
        ordering = ('-created_date', )
        verbose_name_plural = "1. Guest All Information"


post_save.connect(journal_save_handler, sender=GuestInfo)
post_delete.connect(journal_delete_handler, sender=GuestInfo)


class PersonalManager(ChangeloggableMixin, models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE, verbose_name='Mehmon', related_name='personal_managers')
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE, related_name='personal_manager',
                                        verbose_name='Taklif qiluvchi tashkilot nomi')
    personal_manager = models.CharField(max_length=100, verbose_name='Mas\'ul shaxs')
    personal_manager_phone = models.CharField(max_length=9, verbose_name='Mas\'ul shaxsning\ntelefon raqami')

    def __str__(self):
        return f'{self.personal_manager}  ||  {self.company_offered}'

    class Meta:
        ordering = ('-date', )
        verbose_name_plural = "2. Personal Manager"


post_save.connect(journal_save_handler, sender=PersonalManager)
post_delete.connect(journal_delete_handler, sender=PersonalManager)


class VisaCity(ChangeloggableMixin, models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE, verbose_name='Mehmon', related_name='mid')
    pass_visa_date = models.DateField(null=True, blank=True, verbose_name='Vizaga hujjat topshirilgan sana')
    present_visa_date = models.DateField(null=True, blank=True, verbose_name='Viza taqdim etilgan sana')
    guest_come_date = models.DateField(null=True, blank=True, verbose_name='Mehmon keldi')
    guest_back_date = models.DateField(null=True, blank=True, verbose_name='Mehmon keldi')
    price = models.FloatField(null=True, blank=True, verbose_name='Narxi', default=300000.0)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Agent')
    payment_type = models.CharField(choices=payment, default='transfer', max_length=50,
                                            verbose_name='To\'lov statusi')
    visa_days = models.CharField(max_length=100, null=True, blank=True, verbose_name='Visa olingan kundan')
    status = models.CharField(max_length=100, null=True, blank=True, verbose_name='Holati')


    def __str__(self):
        return f'Visa to {self.guest}'

    def get_foreign_company(self):
        return self.guest.foreign_company
    get_foreign_company.short_description = 'Xorijiy tashkilot'

    def get_company_offered(self):
        company_offered = PersonalManager.objects.get(guest_id=self.guest_id)
        return company_offered.company_offered
    get_company_offered.short_description = 'Taklif qiluvchi tashkilot'

    def get_passport(self):
        return self.guest.passport_id
    get_passport.short_description = 'Passport'

    def get_citizenship(self):
        return self.guest.citizenship
    get_citizenship.short_description = 'Fuqaroligi'

    class Meta:
        ordering = ('-date', )
        verbose_name_plural = "3. Visa City"


post_save.connect(journal_save_handler, sender=VisaCity)
post_delete.connect(journal_delete_handler, sender=VisaCity)


class AirTicket(ChangeloggableMixin, models.Model):
    citizen = (
        ('foreign', 'Ne Rezident'),
        ('local', 'Rezident'),
    )
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE, verbose_name='Mehmon', related_name='airtickets')
    guest_full_name_visa = models.CharField(max_length=100, verbose_name='FISH', null=True, blank=True)
    citizen = models.CharField(choices=citizen, default='foreign', max_length=50, verbose_name='Fuqaroligi')
    trip_goal = models.CharField(max_length=255, null=True, blank=True, verbose_name='Safar maqsadi',
                                 default='Muzokaralar uchun')
    flight = models.CharField(max_length=20, verbose_name='Reys')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Davlati')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Agent')
    ticket_office = models.CharField(max_length=100, verbose_name='Aviakassa')
    flight_come_date = models.DateField(verbose_name='Kelgan reys', null=True, blank=True)
    flight_back_date = models.DateField(verbose_name='Ketgan reys', null=True, blank=True)
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE, verbose_name='Aviatashuvchi')
    price = models.FloatField(null=True, blank=True, verbose_name='Bilet narxi')
    payment_type = models.CharField(choices=payment, default='transfer', max_length=50,  verbose_name='To\'lov statusi')

    def __str__(self):
        return f'Ticket to {self.guest}'

    def get_company_offered(self):
        company_offered = PersonalManager.objects.get(guest_id=self.guest_id)
        return company_offered.company_offered
    get_company_offered.short_description = 'Taklif qiluvchi tashkilot'

    def get_personal_manager(self):
        personal_manager = PersonalManager.objects.get(guest_id=self.guest_id)
        return personal_manager.personal_manager
    get_personal_manager.short_description = 'Buyurtmachi'

    class Meta:
        ordering = ('-date', )
        verbose_name_plural = "4. Air Ticket"


post_save.connect(journal_save_handler, sender=AirTicket)
post_delete.connect(journal_delete_handler, sender=AirTicket)


class Hotel(ChangeloggableMixin, models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE, verbose_name='Mehmon', related_name='hotels')
    hotel_name = models.CharField(max_length=100, verbose_name='Mehmonxona')
    guest_come_date = models.DateField(verbose_name='Mexmon kirgan kuni', default=timezone.now, null=True, blank=True)
    guest_back_date = models.DateField(verbose_name='Mexmon chiqqan kuni', null=True, blank=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Agent')
    price = models.FloatField(null=True, blank=True, verbose_name='Narxi (so\'mda)')
    hotel_days = models.CharField(max_length=100, null=True, blank=True, verbose_name='Yashagan kunlar')
    payment_type = models.CharField(choices=payment, default='transfer', max_length=50, verbose_name='To\'lov statusi')

    def __str__(self):
        return f'Hotel to {self.guest}'

    def get_citizenship(self):
        return self.guest.citizenship
    get_citizenship.short_description = 'Fuqaroligi'

    def get_company_offered(self):
        company_offered = PersonalManager.objects.get(guest_id=self.guest_id)
        return company_offered.company_offered
    get_company_offered.short_description = 'Taklif qiluvchi tashkilot'

    def get_personal_manager(self):
        personal_manager = PersonalManager.objects.get(guest_id=self.guest_id)
        return personal_manager.personal_manager
    get_personal_manager.short_description = 'Buyurtmachi'

    class Meta:
        ordering = ('-date', )
        verbose_name_plural = "5. Hotel"


post_save.connect(journal_save_handler, sender=Hotel)
post_delete.connect(journal_delete_handler, sender=Hotel)


class OtherDocument(ChangeloggableMixin, models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE, verbose_name='Mehmon', related_name='others')
    price = models.FloatField(null=True, blank=True,  verbose_name='Narxi (so\'mda)')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Agent')
    payment_type = models.CharField(choices=payment, default='transfer', max_length=50,
                                            verbose_name='To\'lov statusi')

    def __str__(self):
        return f'Other Documents to {self.guest}'

    def get_citizenship(self):
        return self.guest.citizenship
    get_citizenship.short_description = 'Fuqaroligi'

    def get_company_offered(self):
        company_offered = PersonalManager.objects.get(guest_id=self.guest_id)
        return company_offered.company_offered
    get_company_offered.short_description = 'Taklif qiluvchi tashkilot'

    def get_trip_goal(self):
        trip_goal = AirTicket.objects.get(guest_id=self.guest_id)
        return trip_goal.trip_goal
    get_trip_goal.short_description = 'Safar maqsadi'

    class Meta:
        ordering = ('-date', )
        verbose_name_plural = "6. Other Documents"


post_save.connect(journal_save_handler, sender=OtherDocument)
post_delete.connect(journal_delete_handler, sender=OtherDocument)


class VisaControl(ChangeloggableMixin, models.Model):
    status = (
        ('come', 'Keldi'),
        ('leave', 'Qaytib ketti'),
        ('not_come', 'Kelmadi'),
    )
    living_address_type = (
        ('hotel', 'Hotel'),
        ('flat', 'Kvartira'),
        ('container', 'Konteyner'),
    )
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE, verbose_name='Mehmon')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Agent')
    guest_come_date = models.DateField(null=True, blank=True, verbose_name='Mehmon keldi')
    guest_back_date = models.DateField(null=True, blank=True, verbose_name='Mehmon ketdi')
    guest_living_address = models.CharField(null=True, blank=True, max_length=255,
                                            verbose_name='Istiqomat qilayotgan manzil')
    guest_living_address_type = models.CharField(null=True, blank=True, choices=living_address_type, default='flat',
                                                 max_length=50, verbose_name='Yashash joyi turi')
    registration_date = models.DateField(null=True, blank=True, verbose_name='Propiska muddati')
    visa_validate_date = models.DateField(null=True, blank=True, verbose_name='Visa amal qilish muddati')
    license_date = models.DateField(null=True, blank=True, verbose_name='Litsenziya muddati')
    possible_leave_date = models.DateField(null=True, blank=True, verbose_name='Ehtimoliy ketish kuni')
    # note = models.CharField(max_length=255, null=True, blank=True, verbose_name='Eslatma')
    visa_days = models.CharField(max_length=100, null=True, blank=True, verbose_name='Kunlar soni')
    guest_status = models.CharField(choices=status, max_length=50, default='come',
                                    verbose_name='keldi/Ketdi')

    def __str__(self):
        return f'Visa to {self.guest}'

    def get_company_offered(self):
        company_offered = PersonalManager.objects.get(guest_id=self.guest_id)
        return company_offered.company_offered
    get_company_offered.short_description = 'Taklif qiluvchi tashkilot'

    def get_citizenship(self):
        return self.guest.citizenship
    get_citizenship.short_description = 'Fuqaroligi'

    def get_personal_manager(self):
        personal_manager = PersonalManager.objects.get(guest_id=self.guest_id)
        return personal_manager.personal_manager
    get_personal_manager.short_description = 'Buyurtmachi'

    class Meta:
        ordering = ('-date', )
        verbose_name_plural = "7. Visa Control"


post_save.connect(journal_save_handler, sender=VisaControl)
post_delete.connect(journal_delete_handler, sender=VisaControl)
