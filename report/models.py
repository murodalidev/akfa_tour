from django.db import models
from django.db.models.signals import post_delete, post_save
from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler
from database.models import CompanyOffered, Country


class TotalReport(ChangeloggableMixin, models.Model):
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE, verbose_name='Tashkilot')
    total = models.FloatField(null=True, blank=True, default=0)

    class Meta:
        verbose_name_plural = "1. TotalReport"

    def __str__(self):
        return f'{self.company_offered}'


post_save.connect(journal_save_handler, sender=TotalReport)
post_delete.connect(journal_delete_handler, sender=TotalReport)


class AirTicketReport(ChangeloggableMixin, models.Model):
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE, verbose_name='Tashkilot')
    total = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name_plural = "2. AirTicketReport"

    def __str__(self):
        return f'{self.company_offered}'


post_save.connect(journal_save_handler, sender=AirTicketReport)
post_delete.connect(journal_delete_handler, sender=AirTicketReport)


class GuestReport(ChangeloggableMixin, models.Model):
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE, verbose_name='Tashkilot')
    total = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name_plural = "3. GuestReport"

    def __str__(self):
        return f'{self.company_offered}'


post_save.connect(journal_save_handler, sender=GuestReport)
post_delete.connect(journal_delete_handler, sender=GuestReport)


class HotelReport(ChangeloggableMixin, models.Model):
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE, verbose_name='Tashkilot')
    total = models.FloatField(null=True, blank=True, default=0.00)

    class Meta:
        verbose_name_plural = "4. HotelReport"

    def __str__(self):
        return f'{self.company_offered}'


post_save.connect(journal_save_handler, sender=HotelReport)
post_delete.connect(journal_delete_handler, sender=HotelReport)


class ServiceReportMid(ChangeloggableMixin, models.Model):
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE, verbose_name='Tashkilot')
    total = models.FloatField(null=True, blank=True, default=0.00)

    class Meta:
        verbose_name_plural = "5.1 ServiceReportMid"

    def __str__(self):
        return f'{self.company_offered}'


post_save.connect(journal_save_handler, sender=ServiceReportMid)
post_delete.connect(journal_delete_handler, sender=ServiceReportMid)


class ServiceReportPradVisa(ChangeloggableMixin, models.Model):
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE, verbose_name='Tashkilot')
    total = models.FloatField(null=True, blank=True, default=0.00)

    class Meta:
        verbose_name_plural = "5.2 ServiceReportPradVisa"

    def __str__(self):
        return f'{self.company_offered}'


post_save.connect(journal_save_handler, sender=ServiceReportPradVisa)
post_delete.connect(journal_delete_handler, sender=ServiceReportPradVisa)


class ServiceReportReg(ChangeloggableMixin, models.Model):
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE, verbose_name='Tashkilot')
    total = models.FloatField(null=True, blank=True, default=0.00)

    class Meta:
        verbose_name_plural = "5.3 ServiceReportReg"

    def __str__(self):
        return f'{self.company_offered}'


post_save.connect(journal_save_handler, sender=ServiceReportReg)
post_delete.connect(journal_delete_handler, sender=ServiceReportReg)


class ServiceReportLicence(ChangeloggableMixin, models.Model):
    company_offered = models.ForeignKey(CompanyOffered, on_delete=models.CASCADE, verbose_name='Tashkilot')
    total = models.FloatField(null=True, blank=True, default=0.00)

    class Meta:
        verbose_name_plural = "5.4 ServiceReportLicence"

    def __str__(self):
        return f'{self.company_offered}'


post_save.connect(journal_save_handler, sender=ServiceReportLicence)
post_delete.connect(journal_delete_handler, sender=ServiceReportLicence)


# class ServiceReportResident(models.Model):
#     # country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country')
#     # total = models.FloatField(null=True, blank=True, default=0.00)
#     pass
#
#     class Meta:
#         verbose_name_plural = "5.5 ServiceReportResident"


