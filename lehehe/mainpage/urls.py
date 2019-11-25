#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:30:08 2019

@author: dongdong
"""

from django.urls import path
from . import views
app_name = 'mainpage'
urlpatterns = [
    path(r'', views.page_list, name='page_list'),
]