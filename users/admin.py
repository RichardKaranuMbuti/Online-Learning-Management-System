from .models import CustomUserModel
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    ordering = ['-date_created',]
    list_filter = [
        'username',
        'email',
        'date_created',
        'is_staff',
        'is_superuser',
	]
    list_display = [
		'uid',
		'first_name',
		'last_name',
		'username',
		'email',
		'phone_number',
		'date_created',
		'is_staff',
		'is_active',
        'is_superuser',
	]
    fieldsets = (
		("User Detials", {
			"fields": (
				'first_name',
                'last_name',
                'username',
                'email',
                'phone_number',
			),
		}),
        ("Permissions", {
            "fields": (
                'is_active',
                'is_superuser',
                'is_staff',
			),
		}),
	)
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                'first_name',
                'last_name',
                'username',
                'email',
                'password1',
                'password2',
                'is_staff',
                'is_superuser',
			),
		}),
	)

admin.site.register(CustomUserModel, CustomUserAdmin)
