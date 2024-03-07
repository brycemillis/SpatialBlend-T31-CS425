from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class ImageUploadForm(forms.Form):
    image1 = forms.ImageField(label='Image 1')
    image2 = forms.ImageField(label='Image 2')