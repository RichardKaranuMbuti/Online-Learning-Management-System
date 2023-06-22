from django.contrib import admin
from .models import Department, Unit

# Register your models here.
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
	list_display = ['name', 'code', 'department', 'description']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
	list_display = ['name', 'code', 'description']

