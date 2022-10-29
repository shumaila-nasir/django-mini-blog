from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post

class SignupForm(UserCreationForm):
    fname = forms.CharField(max_length=100, label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    lname = forms.CharField(max_length=100, label='Last Name',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model= User
        fields = ['username', 'fname', 'lname', 'email']
        widgets = {
                    'username':forms.TextInput(attrs={'class':'form-control'}),
                    # 'fname': forms.TextInput(attrs={'class': 'form-control'}),
                    # 'lname': forms.TextInput(attrs={'class': 'form-control'}),
                    # 'email': forms.EmailInput(attrs={'class': 'form-control'}),

                   }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget= forms.TextInput(attrs={'autofocus':True, 'class': 'form-control'}))
    password = forms.CharField(label=_("password"), strip=False,
                                    widget=forms.PasswordInput(attrs=
                                {'autocomplete': 'current_password', 'class': 'form-control'}))


class PostForm(forms.ModelForm):
    # description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Post
        fields = ['title', 'description']
        labels = {'title': 'Title', 'description': 'Description'}
        widgets = {
                    'title':forms.TextInput(attrs={'class': 'form-control'}),
                    'description':forms.Textarea(attrs={'class': 'form-control'}),
                   }