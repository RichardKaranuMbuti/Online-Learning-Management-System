from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    mobile_number = forms.IntegerField(required=True, widget=forms.TextInput)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'mobile_number',
            'email',
            'username',
            'password1',
            'password2'
            )

class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
