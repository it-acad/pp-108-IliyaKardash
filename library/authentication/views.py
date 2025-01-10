from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.hashers import make_password
from authentication.models import CustomUser
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')

        errors = []

        if not first_name or not last_name or not email or not password or not confirm_password:
            errors.append('Required fields are empty')
        if password != confirm_password:
            errors.append('Password doesn\'t match')
        if CustomUser.objects.filter(email=email).exists():
            errors.append('User with this email already exists')
        if CustomUser.objects.filter(first_name=first_name, last_name=last_name).exists():
            errors.append('User already exists')

        if not errors:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                role=int(role),
                middle_name='',
                password=password,
                is_active=True
            )
            user.save()
            login(request, user)
            return redirect('login')

        return render(request, 'authentication/register.html', {'errors': errors})

    return render(request, 'authentication/register.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Email: {email}, Password: {password}")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'authentication/login.html', {'error': 'Invalid email or password'})

    return render(request, 'authentication/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')
