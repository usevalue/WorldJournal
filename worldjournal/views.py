from django.shortcuts import render

def welcome(request):
    return render(request, 'welcome.html')

def userpage(request):
    return render(request,'welcome.html');