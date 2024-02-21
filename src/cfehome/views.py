from django.shortcuts import render


def home_view(request):
    return render(request, "pages/home.html", {})

def about_us_view(request):
    return render(request, "pages/aboutUs.html", {})

def image_combine_view(request):
    return render(request, "pages/imageCombine.html", {})

def image_editor_view(request):
    return render(request, "pages/imageEditor.html", {})

def login_view(request):
    return render(request, "pages/login.html", {})

def recent_blends_view(request):
    return render(request, "pages/recentBlends.html", {})

def signup_view(request):
    return render(request, "pages/signup.html", {})