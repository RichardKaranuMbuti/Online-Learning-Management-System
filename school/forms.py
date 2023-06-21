from django.forms import ModelForm
from .models import Department, Unit

class DepartmentCreationForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'code', 'description']

class UnitCreationForm(ModelForm):
    class Meta:
        model = Unit
        fields = "__all__"