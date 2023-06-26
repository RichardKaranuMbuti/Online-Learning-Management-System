from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from .managers import CustomUserManager


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
	uid = models.AutoField(_("user id"), primary_key=True)
	first_name = models.CharField(_("first name"), max_length=50)
	last_name = models.CharField(_("last name"), max_length=50)
	username = models.CharField(_("username"), max_length=50, unique=True)
	email = models.EmailField(_("email address"), max_length=254, unique=True)
	phone_number = models.CharField(_("phone number"), max_length=10)
	date_created = models.DateField(_("date joined"), default=timezone.now, editable=False)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)
	
	objects = CustomUserManager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']


	def __str__(self) -> str:
		return self.first_name + ' ' + self.last_name
