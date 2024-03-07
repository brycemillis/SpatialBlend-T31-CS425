from io import BytesIO

from PIL import Image
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CreateUserForm, ImageUploadForm
from .image_processing import create_hybrid_image


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
    context = {}
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image1 = Image.open(request.FILES['image1'])
            image2 = Image.open(request.FILES['image2'])
            hybrid_image = create_hybrid_image(image1, image2, low_pass_cutoff=20, high_pass_cutoff=40)

            # Convert PIL image to byte array
            image_io = BytesIO()
            hybrid_image.save(image_io, format='PNG')
            image_io.seek(0)

            # Save the hybrid image in Django's default storage (usually media folder)
            filename = 'hybrid_images/hybrid_image_result.png'
            default_storage.save(filename, ContentFile(image_io.getvalue()))

            # Generate the URL for downloading
            hybrid_image_url = default_storage.url(filename)
            context['hybrid_image_url'] = hybrid_image_url
    else:
        form = ImageUploadForm()
    
    context['form'] = form
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