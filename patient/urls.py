from django.urls import path
from . import views

urlpatterns = [
    path("", views.home , name="home"),
    path("doctor_login/", views.doctor_login , name="doctor_login"),
    path("doctor_logout/", views.doctor_logout , name="doctor_logout"),
    path("reset_password/", views.doctor_reset_password, name="doctor_reset_password"),
    path("doctor_dashboard/", views.doctor_dashboard, name="doctor_dashboard"),
    path("add_patient_form/", views.add_patient_form, name="add_patient_form"),
    

   
]

