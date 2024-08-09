from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
def register_user(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email']
        )
        return redirect('login_user')
    return render(request, 'dashboard/login/login.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('attendance')
        else:
            return redirect('error')
    return render(request, 'dashboard/login/login.html')

# Foydalanuvchini tizimdan chiqarish uchun view
def log_out(request):
    logout(request)
    return redirect('login_user')

# Xatolik yuz berganda ko'rsatiladigan sahifa uchun view
def error(request):
    return render(request, 'dashboard/login/error.html')