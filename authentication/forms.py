from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

from authentication.models import Gender

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class UserRegisterForm(UserCreationForm):
    """
        Creates User registration form for signing up.
    """
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={
        "name": "email", "class": "input100",
        "placeholder": "Email"
    }
    ),
        help_text='Required. Input a valid email address.'
    )
    password1 = forms.CharField(label="Password",
    widget=forms.PasswordInput(attrs={
        "name": "password", "class": "input100",
        "placeholder": "Password"
    }
    ),
    )

    password2 = forms.CharField(label="Confirm Password",
                                help_text=_(
                                    "Enter the same password as before, for verification."),
    widget=forms.PasswordInput(attrs={"name": "Confirm Password", "class": "input100", "placeholder": "Confirm Password"}),
    )
    MEMBER_CHOICE= (
        ("Worker", "Worker"),
        ("New Convert", "New Convert"),
        ("Member", "Member"),
    )
    status = forms.ChoiceField(choices = MEMBER_CHOICE, required=True, label=_("Status"))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'status']
        widgets = {

            "username": forms.TextInput(attrs={
                "name": "username", "class": "input100",
                "placeholder": "Username"
            }),
        }

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class CustomUserEditForm(UserEditForm):
    country = forms.CharField(required=False, label=_("Country"))
    MEMBER_CHOICE= (
        ("Worker", "Worker"),
        ("New Convert", "New Convert"),
        ("Member", "Member"),
    )
    status = forms.ChoiceField(choices = MEMBER_CHOICE, required=True, label=_("Status"))
    region = forms.CharField(required=False, label=_("State"))
    gender = forms.ModelChoiceField(queryset=Gender.objects, required=False, label=_("Gendertatus"))
    phone_number = forms.CharField(required=False, label=_("Phone number"))
    residential_address = forms.CharField(required=False, label=_("Residential address"))
    date_of_birth = forms.DateField(required=False)
    avatar = forms.ImageField(required=False, label=_("Avatar"))


class CustomUserCreationForm(UserCreationForm):
    country = forms.CharField(required=False, label=_("Country"))
    MEMBER_CHOICE= (
        ("Worker", "Worker"),
        ("New Convert", "New Convert"),
        ("Member", "Member"),
    )
    status = forms.ChoiceField(choices = MEMBER_CHOICE, required=True, label=_("Status"))
    region = forms.CharField(required=False, label=_("State"))
    gender = forms.ModelChoiceField(queryset=Gender.objects, required=False, label=_("Gender"))
    phone_number = forms.CharField(required=False, label=_("Phone number"))
    residential_address = forms.CharField(required=False, label=_("Residential address"))
    date_of_birth = forms.DateField(required=False)
    avatar = forms.ImageField(required=False, label=_("Avatar"))