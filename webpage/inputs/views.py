from django.views.generic import ListView
from .models import Employee

class EmployeeListView(ListView):
    model = Employee
    template_name = 'inputs_list.html'
    context_object_name = 'page_obj'
