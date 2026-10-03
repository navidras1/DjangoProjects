from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib import messages

from .forms import CreateUserForm, LoginForm, UpdateUserForm
from .tokens import account_activation_token


# Create your views here.
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user= form.save()
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = "verify email to activate your account"
            message = render_to_string('email-verification.html',{
                'user':user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('email_verification_sent')
            # return redirect('/ecom/')
    return  render(request,'register.html', {'form': form})

def email_verification(request,uidb64,token):
    unique_id = force_str( urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=unique_id)
    if user and account_activation_token.check_token(user, token):
        user.is_active=True
        user.save()
        return redirect('email_verification_success')
    else:
        return redirect('email_verification_faild')
    pass

def email_verification_success(request):
    return render(request, 'email-verification-success.html')

def email_verification_faild(request):
    return  render(request, 'email-verification-faild.html')
def email_verification_sent(request):
    return render(request, 'email-verification-sent.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('ecom:index')
    else:
        form = LoginForm(request)
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('ecom:index')

@login_required
def profile(request):
    if request.method == 'POST':
        userForm = UpdateUserForm(request.POST, instance=request.user)
        if userForm.is_valid():
            userForm.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('users:profile')
    else:
        userForm = UpdateUserForm(instance=request.user)

    return render(request, 'profile.html', {'userForm': userForm})


