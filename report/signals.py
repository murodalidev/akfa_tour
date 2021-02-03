from django.db.models.signals import post_save
from report.models import *
from database.models import CompanyOffered


def company_offered_signal(sender, instance, created, **kwargs):
    if created:
        AirTicketReport.objects.create(
            company_offered=instance
        )
        GuestReport.objects.create(
            company_offered=instance
        )
        HotelReport.objects.create(
            company_offered=instance
        )
        TotalReport.objects.create(
            company_offered=instance
        )
        ServiceReportMid.objects.create(
            company_offered=instance
        )
        ServiceReportPradVisa.objects.create(
            company_offered=instance
        )
        ServiceReportReg.objects.create(
            company_offered=instance
        )
        ServiceReportLicence.objects.create(
            company_offered=instance
        )
        # ServiceReportResident.objects.create(
        #     company_offered=instance
        # )


post_save.connect(company_offered_signal, sender=CompanyOffered)
