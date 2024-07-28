from django.contrib import admin
from django.urls import path
from hospital.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('', IndexView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    ## Doctor View
    path('view_doctor/', DoctorView.as_view(), name='view_doctor'),
    path('<int:pk>/update', UpdateDoctorView.as_view(), name='update_doctor'),
    path('<int:pk>/delete', DeleteDoctorView.as_view(), name='delete_doctor'),
    path('add/', AddDoctorView.as_view(), name='add_doctor'),
]
