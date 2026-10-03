from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomPasswordResetForm, CustomSetPasswordForm

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name="register"),
    path('email-verification/<uidb64>/<token>', views.email_verification, name='email_verification'),
    path('email-verification-sent/',views.email_verification_sent, name='email_verification_sent'),
    path('email-verification-success/',views.email_verification_success, name='email_verification_success'),
    path('email-verification-faild/',views.email_verification_faild, name='email_verification_faild'),
    path('login/', views.user_login, name='login'),
    path('profile/',views.profile,name='profile' ),
    path('logout/', views.user_logout, name='logout'),

    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt',
            success_url=reverse_lazy('users:password_reset_done'),
            form_class=CustomPasswordResetForm,
        ),
        name='password_reset',
    ),
path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html',
            success_url=reverse_lazy('users:password_reset_complete'),
            form_class = CustomSetPasswordForm
        ),
        name='password_reset_confirm',
    ),
    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
]