from django.shortcuts import render
from .forms import UnitCreationForm, DepartmentCreationForm

# Create your views here.


def DepartmentRegistrationView(request):
    form = DepartmentCreationForm()
    context = {"form": form}
    return render(request, "department.html", context)

def UnitRegistrationView(request):
    form = DepartmentCreationForm()
    context = {"form": form}
    return render(request, "unit.html", context)