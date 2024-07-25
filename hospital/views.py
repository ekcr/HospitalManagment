from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, RedirectView
from django.shortcuts import redirect, render
from hospital.models import Doctors
class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    login_url = reverse_lazy('login')

class LoginView(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return render(self.request, 'index.html')
        else:
            form.add_error(None, "Invalid username or password")
            return render(self.request, 'index.html')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(self.request, 'index.html')
        return super().dispatch(request, *args, **kwargs)

class LogoutView(RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return super().get(request, *args, **kwargs)

class DoctorView(LoginRequiredMixin, TemplateView):
    template_name = "view_doctor.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctors.objects.all()
        return context