from django.contrib import admin
from .models import UserModel

# Register your models here.
@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        'uid',
		'first_name',
        'last_name',
        'mobile_number',
        'email',
        'username',
        ]

