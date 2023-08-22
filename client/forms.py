from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    phone = forms.CharField(max_length=15, required=True, help_text='Required.')
    address = forms.CharField(max_length=100, required=True, help_text='Required.')
    medicare_number = forms.CharField(max_length=12, required=True, help_text='Required. Enter your Medicare number.')
    profile_pic = forms.ImageField(required=False, help_text='Upload a profile picture.')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'address', 'medicare_number', 'profile_pic', 'password1', 'password2')
