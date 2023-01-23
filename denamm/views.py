from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def appoinment(request):
    return render(request, 'appoinment.html')

def blogsidebar(request):
    return render(request, 'blogsidebar.html')

def blogsingle(request):
    return render(request, 'blogsingle.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def contact(request):
    return render(request, 'contact.html')

def department(request):
    return render(request, 'department.html')

def departmentsingle(request):
    return render(request, 'departmentsingle.html')

def doctor(request):
    return render(request, 'doctor.html')

def doctorsingle(request):
    return render(request, 'doctorsingle.html')

def service(request):
    return render(request, 'service.html')