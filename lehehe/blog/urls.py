#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:32:12 2019

@author: dongdong
"""

from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path(r'', views.blog_list, name='blog_list'),
    path(r'<int:algo_id>/', views.blog_detail, name='blog_detail'),
]