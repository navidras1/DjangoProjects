from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply the Tailwind class to every widget
        for field in self.fields.values():
            existing = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'auth-field__input {existing}'.strip()

class LoginForm(AuthenticationForm):
    username = forms.CharField( widget=forms.TextInput())
    password = forms.CharField( widget=forms.PasswordInput())