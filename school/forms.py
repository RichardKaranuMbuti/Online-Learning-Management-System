from django.forms import ModelForm
from .models import DepartmentModel, UnitModel


class DepartmentForm(ModelForm):
	class Meta:
		model = DepartmentModel
		fields = (
			"name",
			"code",
			"description"
			)


class UnitForm(ModelForm):
	class Meta:
		model = UnitModel
		exclude = ['slug',]
