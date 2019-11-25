#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:23:33 2019

@author: dongdong
"""

from django import forms
from .models import ArticleColumn,AlgorithmPost,MyalgoPost


class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ("column",)
        
class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = AlgorithmPost
        fields = ("title", "body")
        
class MyalgoPostPostForm(forms.ModelForm):
    class Meta:
        model = MyalgoPost
        exclude = ['author',
                   'column','algo_column','slug'] 
        #fields = ("title", "initial_capital","start_date","end_date","portfolio",
        #          "benchmark","balanced_dates")    
        