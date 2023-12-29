from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

from authentication.models import MembershipStatus,Gender


class CustomUserEditForm(UserEditForm):
    country = forms.CharField(required=False, label=_("Country"))
    status = forms.ModelChoiceField(queryset=MembershipStatus.objects, required=True, label=_("Status"))
    region = forms.CharField(required=False, label=_("State"))
    gender = forms.ModelChoiceField(queryset=Gender.objects, required=False, label=_("Gendertatus"))
    phone_number = forms.CharField(required=False, label=_("Phone number"))
    residential_address = forms.CharField(required=False, label=_("Residential address"))
    date_of_birth = forms.DateField()


class CustomUserCreationForm(UserCreationForm):
    country = forms.CharField(required=False, label=_("Country"))
    status = forms.ModelChoiceField(queryset=MembershipStatus.objects, required=True, label=_("Status"))
    region = forms.CharField(required=False, label=_("State"))
    gender = forms.ModelChoiceField(queryset=Gender.objects, required=False, label=_("Gender"))
    phone_number = forms.CharField(required=False, label=_("Phone number"))
    residential_address = forms.CharField(required=False, label=_("Residential address"))
    date_of_birth = forms.DateField()