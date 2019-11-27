#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:53:19 2019

@author: dongdong
"""

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

from django.contrib.auth.models import User
from .models import UserProfile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "birth")
        
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(label="ConfirmPassword", widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ("username", "email")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.TextInput(attrs={'class': 'input'}),
        }
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("两次输入的密码不匹配")
        return cd['password2']
    
    
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school", "company", "profession", "address", "aboutme")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)
        
        

