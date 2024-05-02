<<<<<<< Updated upstream
=======
from io import BytesIO
from multiprocessing import context

from PIL import Image
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
>>>>>>> Stashed changes
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import CreateUserForm

def home_view(request):
    context = {}
    return render(request, "pages/home.html", context)

def about_us_view(request):
    context = {}
    return render(request, "pages/aboutUs.html", context)

def image_combine_view(request):
    context = {}
    return render(request, "pages/imageCombine.html", context)

def image_editor_view(request):
    context = {}
    return render(request, "pages/imageEditor.html", context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
        
    context = {}
    return render(request, "pages/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def recent_blends_view(request):
    context = {}
    return render(request, "pages/recentBlends.html", context)

def signup_view(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
    context = {'form':form}
    return render(request, "pages/signup.html", context)

def contact_us(request):
    context = {}
    return render(request, 'pages/contactUs.html', context)

def privacy_policy(request):
    context = {}
    return render(request, 'pages/privacyPolicy.html', context)

def license_policy(request):
    context = {}
    return render(request, 'pages/license.html', context)