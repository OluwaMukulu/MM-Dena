from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path("about/", views.about, name="about"),
    path("appoinment/", views.appoinment, name="appoinment"),
    path("blogsidebar/", views.blogsidebar, name="blogsidebar"),
    path("blogsingle/", views.blogsingle, name="blogsingle"),
    path("confirmation/", views.confirmation, name="confirmation"),
    path("contact/", views.contact, name="contact"),
    path("department/", views.department, name="department"),
    path("departmentsingle/", views.departmentsingle, name="departmentsingle"),
    path("doctor/", views.doctor, name="doctor"),
    path("doctorsingle/", views.doctorsingle, name="doctorsingle"),
    path("service/", views.service, name="service"),
]
