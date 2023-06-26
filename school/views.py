from typing import Any, Dict
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .forms import DepartmentForm, UnitForm
from .models import UnitModel, DepartmentModel

# Create your views here.
class HomepageView(TemplateView):
    template_name = 'school/home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["units"] = UnitModel.objects.all()
        return context

class DepartmentView(View):
    template_name = 'school/department.html'
    form_class = DepartmentForm

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>SUCCESS!</h1>")
        return render(request, self.template_name, context)

class CreateUnitView(CreateView):
    template_name = 'school/create_unit.html'
    form_class = UnitForm
    success_url = reverse_lazy("school:display_units")

class DisplayUnitsView(ListView):
    template_name = 'school/display_units.html'
    model = UnitModel
    context_object_name = "units"

class UnitDetailView(DetailView):
    template_name = 'school/detail_unit.html'
    model = UnitModel
    context_object_name = "unit"

class ManageUnitsView(ListView):
    template_name = 'school/manage_units.html'
    model = UnitModel
    context_object_name = "units"

class EditUnitView(UpdateView):
    template_name = 'school/edit_unit.html'
    model = UnitModel
    form_class = UnitForm
    success_url = reverse_lazy("school:manage_units")

class DeleteUnitView(DeleteView):
    template_name = 'school/confirm_delete_unit.html'
    model = UnitModel
    success_url = reverse_lazy("school:manage_units")
    context_object_name = "unit"

class ContactView(TemplateView):
    template_name = 'school/contact.html'
