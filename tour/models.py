from django.contrib.auth.models import User
from django.utils import timezone

from database.models import *
from django.utils.html import mark_safe

payment = (
    ('transfer', 'Perechesleniya'),
    ('transfer_ok', 'Pereches-OK'),
    ('payed', 'To\'landi'),
    ('not_payed', 'To\'lanmadi'),
)


class GuestInfo(models.Model):
    guest_full_name = models.CharField(max_length=100, verbose_name='FISH')
    passport_id = models.CharField(max_length=15, verbose_name='Passport')
    citizenship = models.ForeignKey(Citizenship, on_delete=models.CASCADE, verbose_name='Fuqaroligi')
    foreign_company = models.CharField(max_length=100, verbose_name='Xorijiy tashkilot nomi')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return self.guest_full_name

    class Meta:
        ordering = ('-created_date', )
        verbose_name_plural = "      Guest All Information"

    # def v_employee(self):
    #     employee = Visa.objects.filter(guest=self.id)
    #     to_return = '<ul style="margin: 0px !important">'
    #     to_return += '\n'.join(
    #         '<li>{}</li>'.format(item.employee) for item in employee)
    #     to_return += '</ul>'
    #     return mark_safe(to_return)
    #
    # v_employee.short_description = 'Xizmat ko\'rsatuvchi xodim'
    #
    # def p_m_c_o(self):
    #     personal = PersonalManager.objects.filter(guest=self.id)
    #     to_return = '<ul style="margin: 0px !important">'
    #     to_return += '\n'.join(
    #         '<li>{}</li>'.format(item.company_offered) for item in personal)
    #     to_return += '</ul>'
    #     return mark_safe(to_return)
    #
    # p_m_c_o.short_description = 'Taklif qiluvchi tashkilot nomi'
    #
    # def v_c_g_come_d(self):
    #     come_date = VisaControl.objects.filter(guest=self.id)
    #     to_return = '<ul style="margin: 0px !important">'
    #     to_return += '\n'.join(
    #         '<li>{}</li>'.format(item.guest_come_date) for item in come_date)
    #     to_return += '</ul>'
    #     return mark_safe(to_return)
    #
    # v_c_g_come_d.short_description = 'Mehmon keldi'
    #
    # def v_c_g_back_d(self):
    #     back_date = VisaControl.objects.filter(guest=self.id)
    #     to_return = '<ul style="margin: 0px !important">'
    #     to_return += '\n'.join(
    #         '<li>{}</li>'.format(item.guest_come_date) for item in back_date)
    #     to_return += '</ul>'
    #     return mark_safe(to_return)
    #
    # v_c_g_back_d.short_description = 'Mehmon ketdi'
    #
    # def v_c_g_l_a(self):
    #     guest_living_address = VisaControl.objects.filter(guest=self.id)
    #     to_return = '<ul style="margin: 0px !important">'
    #     to_return += '\n'.join(
    #         '<li>{}</li>'.format(item.guest_living_address) for item in guest_living_address)
    #     to_return += '</ul>'
    #     return mark_safe(to_return)
    #
    # v_c_g_l_a.short_description = 'Istiqomat qilayotgan manzili'
    #
    # def v_c_g_l_a_t(self):
    #     guest_living_address_type = VisaControl.objects.filter(guest=self.id)
    #     to_return = '<ul style="margin: 0px !important">'
    #     to_return += '\n'.join(
    #         '<li>{}</li>'.format(item.guest_living_address_type) for item in guest_living_address_type)
    #     to_return += '</ul>'
    #     return mark_safe(to_return)
    #
    # v_c_g_l_a_t.short_description = 'Yashash joyi turi'
    #
    # def v_c_r_d(self):
    #     registration_date = VisaControl.objects.filter(guest=self.id)
    #     to_return = '<ul style="margin: 0px !important">'
    #     to_return += '\n'.join(
    #         '<li>{}</li>'.format(item.registration_date) for item in registration_date)
    #     to_return += '</ul>'
    #     return mark_safe(to_return)
    #
    # v_c_r_d.short_description = 'Propiska middati'
    #
    # def v_c_v_v_d(self):
    #     visa_validate_date = VisaControl.objects.filter(guest=self.id)
    #     to_return = '<ul style="margin: 0px !important">'
    #     to_return += '\n'.join(
    #         '<li>{}</li>'.format(item.visa_validate_date) for item in visa_validate_date)
    #     to_return += '</ul>'
    #     return mark_safe(to_return)
    #
    # v_c_v_v_d.short_description = 'Viza amal qilish muddati'
    #
    # def v_c_l_d(self):
    #     license_date = VisaControl.objects.filter(guest=self.id)
    #     to_return = '<ul style="margin: 0px !important">'
    #     to_return += '\n'.join(
    #         '<li>{}</li>'.format(item.license_date) for item in license_date)
    #     to_return += '</ul>'
    #     return mark_safe(to_return)
    #
    # v_c_l_d.short_description = 'Litsenziya muddati'
    #
    # def p_m_p_m(self):
    #     personal_manager = PersonalManager.objects.filter(guest=self.id)
    #     to_return = '<ul style="margin: 0px !important">'
    #     to_return += '\n'.join(
    #         '<li>{}</li>'.format(item.personal_manager) for item in personal_manager)
    #     to_return += '</ul>'
    #     return mark_safe(to_return)
    #
    # p_m_p_m.short_description = 'Taklif qiluvchi tashkilot nomi'
    #
    # def v_c_g_s(self):
    #     guest_status = VisaControl.objects.filter(guest=self.id)
    #     to_return = '<ul style="margin: 0px !important">'
    #     to_return += '\n'.join(
    #         '<li>{}</li>'.format(item.guest_status) for item in guest_status)
    #     to_return += '</ul>'
    #     return mark_safe(to_return)
    #
    # v_c_g_s.short_description = 'Keldi/Ketti'


class PersonalManager(models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE, verbose_name='Mehmon')
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE,
                                        verbose_name='Taklif qiluvchi tashkilot nomi')
    personal_manager = models.CharField(max_length=100, verbose_name='Mas\'ul shaxs')
    personal_manager_phone = models.CharField(max_length=15, verbose_name='Mas\'ul shaxsning\ntelefon raqami')

    def __str__(self):
        return f'{self.personal_manager}  ||  {self.company_offered}'

    class Meta:
        ordering = ('-date', )
        verbose_name_plural = "     Personal Manager"


class VisaCity(models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE, verbose_name='Mehmon')
    pass_visa_date = models.DateField(null=True, blank=True, verbose_name='Vizaga hujjat topshirilgan sana')
    present_visa_date = models.DateField(null=True, blank=True, verbose_name='Viza taqdim etilgan sana')
    guest_come_date = models.DateField(null=True, blank=True, verbose_name='Mehmon keldi')
    guest_back_date = models.DateField(null=True, blank=True, verbose_name='Mehmon keldi')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Agent')
    payment_type_to_visa = models.CharField(choices=payment, default='transfer', max_length=50,
                                            verbose_name='To\'lov statusi')

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
        verbose_name_plural = "    Visa City"


class AirTicket(models.Model):
    citizen = (
        ('foreign', 'Ne Rezident'),
        ('local', 'Rezident'),
    )
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE, verbose_name='Mehmon')
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
    ticket_price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2,
                                       verbose_name='Bilet narxi')
    payment_type_to_ticket = models.CharField(choices=payment, default='transfer', max_length=50,
                                              verbose_name='To\'lov statusi')

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
        verbose_name_plural = "   Air Ticket"


class Hotel(models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE, verbose_name='Mehmon')
    hotel_name = models.CharField(max_length=100, verbose_name='Mehmonxona')
    guest_come_date = models.DateField(verbose_name='Mexmon kirgan kuni', default=timezone.now, null=True, blank=True)
    guest_back_date = models.DateField(verbose_name='Mexmon chiqqan kuni', null=True, blank=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Agent')
    hotel_price_uzs = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2,
                                          verbose_name='Narxi (so\'mda)')
    hotel_price_us = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2,
                                         verbose_name='Narxi ($ da)')
    payment_type_to_hotel = models.CharField(choices=payment, default='transfer', max_length=50,
                                             verbose_name='To\'lov statusi')

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
        verbose_name_plural = "  Hotel"


class OtherDocument(models.Model):
    date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='Sana')
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE, verbose_name='Mehmon')
    visa_price_uzs = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2,
                                         verbose_name='Bilet narxi (so\'mda)')
    visa_price_us = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2,
                                        verbose_name='Bilet narxi ($ da)')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Agent')
    payment_type_to_visa = models.CharField(choices=payment, default='transfer', max_length=50,
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
        verbose_name_plural = " Other Documents"


class VisaControl(models.Model):
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
    guest_back_date = models.DateField(null=True, blank=True, verbose_name='Mehmon keldi')
    guest_living_address = models.CharField(null=True, blank=True, max_length=255,
                                            verbose_name='Istiqomat qilayotgan manzil')
    guest_living_address_type = models.CharField(null=True, blank=True, choices=living_address_type, default='flat',
                                                 max_length=50, verbose_name='Yashash joyi turi')
    registration_date = models.DateField(null=True, blank=True, verbose_name='Propiska muddati')
    visa_validate_date = models.DateField(null=True, blank=True, verbose_name='Visa amal qilish muddati')
    license_date = models.DateField(null=True, blank=True, verbose_name='Litsenziya muddati')
    possible_leave_date = models.DateField(null=True, blank=True, verbose_name='Ehtimoliy ketish kuni')
    note = models.CharField(max_length=255, null=True, blank=True, verbose_name='Eslatma')
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
        verbose_name_plural = "Visa Control"
