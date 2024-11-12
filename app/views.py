import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend suitable for web environments

import matplotlib.pyplot as plt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Count
from django.utils import timezone
from io import BytesIO
import base64
from .models import UserProfile, Task
from admins.models import Events
from leave.models import Leave
import pytz

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import UserProfile, Task
from .forms import UserProfileForm
import pytz

@login_required
def home(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    # Fetch tasks and other details
    tasks = Task.objects.filter(user=request.user)

    if request.method == "POST":
        task_name = request.POST.get('name')
        if task_name:
            Task.objects.create(user=request.user, name=task_name)
            messages.success(request, 'Task added successfully.')

        return redirect('home')

    context = {
        'user': request.user,
        'profile': profile,
        'tasks': tasks,
        'profile_picture': profile.get_profile_picture(),
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        position = request.POST.get('position').strip()
        place = request.POST.get('place').strip()

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'An account with this email already exists.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            UserProfile.objects.create(user=user, position=position, place=place)
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            update_last_login_time(user)
            return redirect('admin_dashboard' if user.username == 'admin' else 'home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def update_last_login_time(user):
    profile = get_object_or_404(UserProfile, user=user)
    profile.last_login_time = timezone.now().astimezone(pytz.timezone('Asia/Kolkata'))
    profile.save()


@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'profile.html', {'profile': user_profile})

@login_required
def tasks(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Task.objects.create(user=request.user, name=name)
            return redirect('home')

    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks.html', {'tasks': tasks})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('home')

@login_required
def approve_leave(request, leave_id):
    update_leave_status(leave_id, 'approved')
    messages.success(request, 'Leave application approved.')
    return redirect('home')

@login_required
def reject_leave(request, leave_id):
    update_leave_status(leave_id, 'rejected')
    messages.success(request, 'Leave application rejected.')
    return redirect('home')

def update_leave_status(leave_id, status):
    """Helper function to update leave status."""
    leave = get_object_or_404(Leave, id=leave_id)
    leave.status = status
    leave.save()
