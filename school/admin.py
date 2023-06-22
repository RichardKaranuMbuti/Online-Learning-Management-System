from django.contrib import admin
from .models import Department, Unit

# Register your models here.
@admin.site.register(Unit)
class UnitAdmin(admin.ModelAdmin):
	pass

@admin.site.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
	pass
