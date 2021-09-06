from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.forms.fields import EmailField
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # check the field name from p manage.py shell , and get the user object , see its attributes
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class UserUpdateForm(forms.ModelForm):  # for updating the username and email
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):  # for updating the profile picture
    class Meta:
        model = Profile
        fields = ['image']
