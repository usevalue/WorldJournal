from django.shortcuts import render

# Create your views here.

def maproom(request):
    return render(request, "maproom.html")