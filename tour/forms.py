from django import forms
from django.forms import inlineformset_factory

from tour.models import PersonalManager, GuestInfo


class GuestInfoForm(forms.ModelForm):
    class Meta:
        model = GuestInfo
        fields = ('guest_full_name', 'foreign_company', 'passport_id', 'citizenship')
        autocomplete_fields = ('citizenship', )


class PersonalManagerForm(forms.ModelForm):
    class Meta:
        model = PersonalManager
        # exclude = ('guest', )
        fields = ('company_offered', 'personal_manager', 'personal_manager_phone')
