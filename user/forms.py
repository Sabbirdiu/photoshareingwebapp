from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30,label= 'User Name :')
    email = forms.EmailField(max_length=200,label= 'Email :')
    password1 = forms.CharField(label='Password: ')
    password2 = forms.CharField(label='Password confirmation: ')
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

