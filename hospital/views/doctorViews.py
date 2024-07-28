from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView, UpdateView, CreateView
from hospital.models import Doctors
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from hospital.forms import DoctorForm

class DoctorView(LoginRequiredMixin, TemplateView):

    template_name = "doctor/view_doctor.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctors.objects.all()
        return context

class DeleteDoctorView(DeleteView, SuccessMessageMixin):
    model = Doctors
    template_name = "doctor/delete_doctor.html" 
    success_message = "Deleted Successfully"
    context_object_name = 'doctor'
    success_url = reverse_lazy('view_doctor')
    
     
class UpdateDoctorView(UpdateView):
    model = Doctors
#     template_name = "doctor/update_doctor.html" 
#     success_message = "Deleted Successfully"
#     context_object_name = 'doctor'
#     success_url = reverse_lazy('view_doctor')


class AddDoctorView(CreateView):
    model = Doctors
    form_class = DoctorForm
    template_name = "doctor/add_doctor.html" 
    success_url = reverse_lazy('view_doctor')

    def form_valid(self, form):
        import ipdb;ipdb.set_trace()
        form.save()
        return super().form_valid(form)