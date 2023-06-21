from django.shortcuts import render, redirect
from django.contrib.auth import views
from django.views import View
from .forms import SignupForm, LoginForm

# Create your views here.
class SignUpView(View):
    def get(self, request):
        form = SignupForm()
        context = {'form': form}
        return render(request, 'users/signup.html', context)

    def post(self, request):
        form = SignupForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('users:login')  # Redirect to OTP confirmation page
        return render(request, 'users/signup.html', context)

    
class LoginView(views.LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    #change to redirect to home page
    next_page = 'users:login'
