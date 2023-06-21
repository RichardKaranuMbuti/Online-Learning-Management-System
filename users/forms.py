from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserModel
from django.contrib.auth.models import User



class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    mobile_number = forms.IntegerField(required=True, widget=forms.TextInput)
    email = forms.CharField(max_length=100, required=True)


    class Meta:
        model = UserModel
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
