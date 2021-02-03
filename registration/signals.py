from django.db.models.signals import post_save
from registration.models import Report
from database.models import CompanyOffered


def company_offered_signal(sender, instance, created, **kwargs):
    if created:
        Report.objects.create(
            company_offered=instance
        )


post_save.connect(company_offered_signal, sender=CompanyOffered)
