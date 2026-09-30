from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name="register"),
    path('email-verification/<uidb64>/<token>', views.email_verification, name='email_verification'),
    path('email-verification-sent/',views.email_verification_sent, name='email_verification_sent'),
    path('email-verification-success/',views.email_verification_success, name='email_verification_success'),
    path('email-verification-faild/',views.email_verification_faild, name='email_verification_faild'),
    path('login/', views.user_login, name='login'),


    path('logout/', views.user_logout, name='logout'),
]