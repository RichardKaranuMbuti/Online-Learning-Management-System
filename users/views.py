from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from django.contrib.auth import views
from django.views import View
from .forms import SignupForm, LoginForm


# Create your views here.
class SignupView(View):
    template_name = 'users/signup.html'
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Replace with Home page
            return HttpResponse("<h1>Success!</h1>")  
        return render(request, self.template_name, context)

class LoginView(views.LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    #change to redirect to home page
    next_page = 'users:login'

    # def get(self, request):
    #     form = self.form_class()
    #     context = {
    #         'form': form
    #     }
    #     return render(request, self.template_name, context)

    # def post(self, request):
    #     form = self.form_class(request, data=request.POST)
    #     context = {
    #         'form': form
    #     }
    #     if form.is_valid():
    #         user = form.get_user()
    #         login(request, user)
    #         # Replace with Home page
    #         return HttpResponse("<h1>Success!</h1>")
    #     return render(request, self.template_name, context)

