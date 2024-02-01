"""cfehome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('aboutUs/', views.about_us_view, name='about_us'),
    path('imageCombine/', views.image_combine_view, name='image_combine'),
    path('imageEditor/', views.image_editor_view, name='image_editor'),
    path('login/', views.login_view, name='login'),
    path('recentBlends/', views.recent_blends_view, name='recent_blends'),
    path('signup/', views.signup_view, name='signup'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # do not do this in prod
    from django.conf.urls.static import static
    
    #Try Django Series
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)