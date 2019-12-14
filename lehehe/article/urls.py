#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:20:19 2019

@author: dongdong
"""
from django.urls import path,re_path
from . import views

app_name = 'article'  # 一定要写这一行，否则html中会报错 'article' is not a registered namespace

urlpatterns = [
    path('myalgo-column/', views.myalgo_column, name="myalgo_column"),
    
    #path('myalgo-opt-detail/', views.myalgo_opt_detail, name="myalgo_opt_detail"),
    path('myalgo-list-to-edit/', views.myalgo_list_to_edit, name="myalgo_list_to_edit"),
    path('myalgo-post/', views.myalgo_post, name="myalgo_post"),
     path('myalgoopt-post/', views.myalgoopt_post, name="myalgoopt_post"),
    path('myalgo-list/', views.myalgo_list, name="myalgo_list"),
    re_path('myalgo-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.myalgo_detail, name="myalgo_detail"),
    path('myalgo-opt/', views.myalgoopt_list, name="myalgoopt_list"),

    path('del-myalgoopt/', views.del_myalgoopt, name="del_myalgoopt"),  
    path('del-myalgo/', views.del_myalgo, name="del_myalgo"),   
    path('redit-myalgo/<int:article_id>/', views.redit_myalgo, name="redit_myalgo"),    
    path('redit-myalgoopt/<int:article_id>/', views.redit_myalgoopt, name="redit_myalgoopt"),   
    re_path('myalgo-opt-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.myalgo_opt_detail, name="myalgo_opt_detail"),
    path('run_test/<int:article_id>/', views.run_test, name="run_test"),
    path('run_algo_opt/<int:algo_opt_id>/', views.run_algo_opt, name="run_algo_opt"),
]