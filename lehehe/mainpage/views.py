from django.shortcuts import render

# Create your views here.

def page_list(request):
    return render(request, "mainpage/page_list.html")