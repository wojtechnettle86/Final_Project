from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Input
from .forms import InputForm, DoctorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import LoggingMixin

class InputListView(ListView):
    model = Input
    template_name = 'inputs_list.html'
    context_object_name = 'page_obj'

class InputDetailView(DetailView):
    model = Input
    template_name = 'inputs_detail.html'

class InputCreateView(CreateView):
    model = Input
    form_class = InputForm
    template_name = 'inputs_form.html'
    success_url = reverse_lazy('input_created')

class InputUpdateView(LoginRequiredMixin, UpdateView, LoggingMixin):
    model = Input
    form_class = DoctorForm
    template_name = 'inputs_form.html'
    success_url = reverse_lazy('inputs_list')

    def form_valid(self, form):
        self.log_action('Update')
        return super().form_valid(form)

class InputDeleteView(LoginRequiredMixin, DeleteView):
    model = Input
    template_name = 'input_confirm_delete.html'
    success_url = reverse_lazy('inputs_list')

def input_created(request):
  return render(request, "input_created.html")
