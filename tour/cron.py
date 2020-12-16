from tour.models import VisaControl


def daily_job():
    daily_minus_one = VisaControl.objects.all()
    for i in daily_minus_one:
        i.visa_validate_date -= 1
        i.save()

