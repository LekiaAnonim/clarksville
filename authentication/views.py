from django.shortcuts import render
from django.contrib.auth.forms import (
    AuthenticationForm,
)
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
UserModel = get_user_model()
from django.contrib.auth.views import (PasswordResetDoneView, PasswordResetConfirmView,
                                        PasswordResetCompleteView, PasswordChangeView,
                                       PasswordChangeDoneView, PasswordResetView)
from .models import User as Member
# Create your views here.
class UserDetail(DetailView):
    model = Member
    template_name = 'courses/profile_detail.html'
    # login_url = "GasApp:login"
    redirect_field_name = "redirect_to"

class UserUpdateView(UpdateView):
    fields = ['username', 'first_name', 'last_name', 'email', 'country', 'region', 'gender', 'status', 'phone_number', 'residential_address', 'date_of_birth', 'avatar']
    model = Member
    template_name = 'authentication/user_update.html'
    # login_url = "GasApp:login"
    redirect_field_name = "redirect_to"
class UserLoginView(View):
    """
     Logs author into dashboard.
    """
    template_name = 'login.html'
    context_object = {"login_form": AuthenticationForm}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):

        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            
            login(request, user)
            messages.success(request, f"Login Successful ! "
                                f"Welcome {user.username}.")
            if user.is_superuser == True:
                return redirect('GasApp:shops')
            
            else:
                shop = get_object_or_404(Shop, user=user)
                return redirect('GasApp:shop-batches', shop.id)

        else:
            messages.error(request,
                           f"Please enter a correct username and password. Note that both fields may be case-sensitive."
                           )
            return render(request, self.template_name, self.context_object)




class PasswordResetView(PasswordResetView):
    template_name = 'registration/pwd_reset_form.html'
    email_template_name = "registration/email_text/password_reset_email.html"
    from_email = ''
    subject_template_name = "registration/email_text/password_reset_subject.txt"
    success_url = reverse_lazy("GasApp:password_reset_done")

class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/email_text/password_reset_done.html' 

class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/email_text/password_reset_confirm.html'
    success_url = reverse_lazy("GasApp:password_reset_complete")

class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/email_text/password_reset_complete.html'

class PasswordChangeView(PasswordChangeView):
    template_name = 'registration/email_text/password_change_form.html'
    success_url = reverse_lazy("GasApp:password_change_done")

class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'registration/email_text/password_change_done.html'

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(
            request, f'Hi {user.username}, your registration was successful!! .')
        return reverse('GasApp:shops')
    else:
        return reverse_lazy('GasApp:email_verification_invalid')


class EmailVerificationConfirm(TemplateView):
    template_name = 'registration/email_verification_confirm.html'


class EmailVerificationInvalid(TemplateView):
    template_name = 'registration/email_verification_invalid.html'