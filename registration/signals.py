from django.db.models.signals import post_save
from registration.models import Report
from database.models import CompanyOffered
from tour.models import VisaCity, PersonalManager
from django.db.models import F


def company_offered(sender, instance, created, **kwargs):
    if created:
        Report.objects.create(
            company_offered=instance
        )


post_save.connect(company_offered, sender=CompanyOffered)


def visa_city(sender, instance, created, **kwargs):

    # if created:
    #     city = VisaCity.objects.all()
    #     for i in city:
    #         for j in Report.objects.all():
    #             if j.company_offered.company_name == i.get_company_offered():
    #                 j.visa_city += 1

    if created:
        for item in Report.objects.all():
            if item.company_offered.company_name == sender.get_company_offered():
                item.visa_city += 1
                item.save()


post_save.connect(visa_city, sender=VisaCity)
