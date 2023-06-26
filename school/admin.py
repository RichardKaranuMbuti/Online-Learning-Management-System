from django.contrib import admin
from .models import DepartmentModel, UnitModel

# Register your models here.
@admin.register(DepartmentModel)
class DepartmentModelAdmin(admin.ModelAdmin):
    list_display = [
		'name',
		'code',
		'description',
	]


@admin.register(UnitModel)
class UnitAdmin(admin.ModelAdmin):
    list_display = [
		'name',
		'creator',
		'rating',
		'price',
		'code',
		'description',
		'department',
	]
    prepopulated_fields = {'slug':('name',),}
