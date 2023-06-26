from django.urls import path
from .views import (
    HomepageView, CreateUnitView, ContactView, 
    DepartmentView, DisplayUnitsView,
    UnitDetailView, ManageUnitsView, EditUnitView, DeleteUnitView)
from users.views import CustomLoginView

app_name = 'school'

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('department/', DepartmentView.as_view(), name='department'),
    path('create_unit/', CreateUnitView.as_view(), name='create_unit'),
    path('units/', DisplayUnitsView.as_view(), name='display_units'),
    path('manage_units/', ManageUnitsView.as_view(), name='manage_units'),
    path('<slug:slug>/', UnitDetailView.as_view(), name='detail_unit'),
    path('edit/<slug:slug>/', EditUnitView.as_view(), name='edit_unit'),
    path('delete/<slug:slug>/', DeleteUnitView.as_view(), name='delete_unit'),
    path('contact/', ContactView.as_view(), name='contact'),
]
