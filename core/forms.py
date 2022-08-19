from dataclasses import fields
from django import forms
from core.models import Post

from cProfile import label

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewPost(forms.ModelForm):
  class Meta:
    model = Post
    fields = '__all__'

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'description': forms.Textarea(attrs={'class': 'form-control', 'col': '40', 'rows': '6'})
    }


class SignupForm(UserCreationForm):
  password1 = forms.CharField(label='Password', widget=forms.PasswordInput(), label_suffix='*')
  password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(), label_suffix='*')
  username = forms.CharField(label_suffix='*')
  first_name = forms.CharField(label_suffix='*')
  email = forms.EmailField(label_suffix='*')
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    labels = {'email': 'Email Address'}

    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'username': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
      'password2': forms.PasswordInput(attrs={'class': 'form-control'})
    }
    
