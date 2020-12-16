from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from tour.forms import GuestInfoForm, PersonalManagerForm
from tour.models import GuestInfo, VisaControl, PersonalManager, VisaCity


def form_view(request):
    if request.method == 'POST':
        guest_form = GuestInfoForm(request.POST)
        personal_manager_form = PersonalManagerForm(request.POST)

        if personal_manager_form.is_valid() and guest_form.is_valid():
            guest_instance = guest_form.save()

            personal_manager_instance = personal_manager_form.save(commit=False)
            personal_manager_instance.guest = guest_instance
            personal_manager_instance.save()

            return redirect('success')
    else:
        guest_form = GuestInfoForm()
        personal_manager_form = PersonalManagerForm()
    context = {'personal_manager_form': personal_manager_form,
               'guest_form': guest_form,
               }
    return render(request, 'tour/form.html', context)


def success_view(request):
    return render(request, 'tour/success.html')
