from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from  .forms import patientForm

# Create your views here.
def home(request):
    return render (request, 'home.html')

# def doctor_login(request):
#     if request.method=="POST":
#         username=request.POST.get("username")
#         password=request.POST.get("password")
#         user=authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('/')
#         else:
#             print('not login in')

#     return render(request, "login.html", {'page_title': "doctor login"})


def doctor_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html", {'page_title': "Doctor Login"})


def doctor_logout(request):
    logout(request)
    return redirect('doctor_login')



@login_required
def doctor_reset_password(request):
    if request.method == "POST":
        password = request.POST.get('password')
        if password:
            request.user.set_password(password)
            request.user.save()
            messages.success(request, 'Password has been changed. Please log in again.')
            return redirect('doctor_login')
        else:
            messages.error(request, 'Please enter a valid password.')
    
    return render(request, "reset-password.html")

def doctor_dashboard(request):
    return render(request,"doctor-dashboard.html")

def add_patient_form(request):
    if request.method=="POST":
        form=patientForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.warning(request, "patient successfully added")
            return redirect("add_patient_form")  
        else:
            messages.warning(request, "something went wrong")
            return redirect("add_patient_form")   
    form=patientForm
    
    return render(request, "add-patient-form.html",{
        'form':form
    })


