from django.urls import path
from .views import SignUpView, CustomLoginView, OTPVerification

app_name = 'users'

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/otp_verification', OTPVerification.as_view(), name='otp'),
]
