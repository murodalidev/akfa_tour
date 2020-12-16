from django.db import models


class Country(models.Model):
    country = models.CharField(max_length=100, verbose_name='Davlat')
    created_date = models.DateTimeField(auto_now_add=True, editable=True, verbose_name='Tizimga iritilgan sana')

    def __str__(self):
        return self.country


class Carrier(models.Model):
    name = models.CharField(max_length=100, verbose_name='Aviatashuvchi')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Tizimga iritilgan sana')

    def __str__(self):
        return self.name


class Citizenship(models.Model):
    citizenship = models.CharField(max_length=50, verbose_name='Fuqaroligi')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Tizimga iritilgan sana')

    def __str__(self):
        return self.citizenship

    def __unicode__(self):
        return self.citizenship


class CompanyOffered(models.Model):
    company_name = models.CharField(max_length=255, verbose_name='Taklif qiluvchi tashkilot nomi')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Tizimga iritilgan sana')

    def __str__(self):
        return self.company_name
