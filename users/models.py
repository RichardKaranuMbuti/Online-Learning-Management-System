from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    uid = models.CharField(max_length=254, primary_key=True)
    mobile_number = models.CharField(max_length=10, blank=False)


    def __str__(self) -> str:
        return super().__str__()
