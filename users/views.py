from django.shortcuts import render, redirect
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(generic.CreateView):
    template_name = 'users/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users:otp")

class CustomLoginView(LoginView):
    template_name = 'school/index.html'
    fields = '__all__',

class OTPVerification(generic.TemplateView):
    template_name = 'users/otp_verification.html'
