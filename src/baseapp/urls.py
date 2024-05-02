from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('aboutUs/', views.about_us_view, name='about_us'),
    path('imageCombine/', views.image_combine_view, name='image_combine'),
    path('imageEditor/', views.image_editor_view, name='image_editor'),
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    
    path('recentBlends/', views.recent_blends_view, name='recent_blends'),
    path('signup/', views.signup_view, name='signup'),
    
<<<<<<< Updated upstream
    path('reset_password/', auth_views.PasswordResetView.as_view(), name = "reset_passwrd"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name = "password_reset_done"),
    path('reset_<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = "password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name = "password_reset_complete"),
    
    # path(images)
=======
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="pages/reset_password.html"), name = "reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="pages/reset_password_sent.html"), name = "password_reset_done"),
    path('reset_<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="pages/reset_password_form.html"), name = "password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="pages/reset_password_complete.html"), name = "password_reset_complete"),
    
    path('contactUs/', views.contact_us, name='contact_us'),
    path('privacyPolicy/', views.privacy_policy, name='privacy_policy'),
    path('license/', views.license_policy, name='license_policy'),
>>>>>>> Stashed changes
]
