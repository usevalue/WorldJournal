from django.shortcuts import render


def shelf(request):
    if request.method == 'POST':
        return render(request, "archive.html")
    else:
        return render(request, "archive.html")
