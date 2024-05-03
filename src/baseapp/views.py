from io import BytesIO

from PIL import Image
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

from .forms import CreateUserForm, ImageUploadForm
from .image_processing import create_hybrid_image
import uuid


def home_view(request):
    context = {}
    return render(request, "pages/home.html", context)

def about_us_view(request):
    context = {}
    return render(request, "pages/aboutUs.html", context)

def learn_more_view(request):
    context = {}
    return render(request, "pages/learnMore.html", context)

def image_combine_view(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image1 = Image.open(request.FILES['image1'])
            image2 = Image.open(request.FILES['image2'])
            hybrid_image = create_hybrid_image(image1, image2)  # Implement the logic for combining images

            image_io = BytesIO()
            hybrid_image.save(image_io, format='PNG', quality=90)
            image_io.seek(0)
            # Generate a unique filename using UUID
            unique_filename = f'hybrid_image_result_{uuid.uuid4().hex}.png'
            default_storage.save(unique_filename, ContentFile(image_io.getvalue()))
            hybrid_image_url = default_storage.url(unique_filename)

            return JsonResponse({'hybrid_image_url': hybrid_image_url})

    # Handle non-AJAX POST request or initial GET request
    form = ImageUploadForm()
    return render(request, "pages/imageCombine.html", {'form': form})

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