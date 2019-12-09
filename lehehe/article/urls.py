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
    path('article-column/', views.article_column, name="article_column"),
    path('myalgo-column/', views.myalgo_column, name="myalgo_column"),
    
    #path('rename-article-column/', views.rename_article_column, name="rename_article_column"),
    #path('del-article-column/', views.del_article_column, name="del_article_column"),
    path('myalgo-list-to-edit/', views.myalgo_list_to_edit, name="myalgo_list_to_edit"),
    path('article-post/', views.article_post, name="article_post"),
    path('article-list/', views.article_list, name="article_list"),
    re_path('article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.article_detail, name="article_detail"),
    path('myalgo-post/', views.myalgo_post, name="myalgo_post"),
    path('myalgo-list/', views.myalgo_list, name="myalgo_list"),
    re_path('myalgo-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.myalgo_detail, name="myalgo_detail"),

    path('del-article/', views.del_article, name="del_article"),   
    path('redit-article/<int:article_id>/', views.redit_article, name="redit_article"),
    
    path('del-myalgo/', views.del_myalgo, name="del_myalgo"),   
    path('redit-myalgo/<int:article_id>/', views.redit_myalgo, name="redit_myalgo"),    
    
    
    path('run_test/<int:article_id>/', views.run_test, name="run_test"),
]