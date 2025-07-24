from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def landing_page(request):
    return render(request, 'landing.html')

def register_page(request):
    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    user = request.user

    if user.role == 'jobseeker':
        return redirect('jobseeker_dashboard')
    elif user.role == 'employer':
        return redirect('employer_dashboard')
    else:
        return redirect('login')

@login_required
def jobseeker_dashboard(request):
    return render(request, 'jobseeker_dashboard.html')

@login_required
def employer_dashboard(request):
    return render(request, 'employer_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')












