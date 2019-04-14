from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from wjlibrary.models import Author


def welcome(request):
    if request.user.is_authenticated:
        try:
            author = Author.objects.get(username=request.user.username)
            return render(request, 'welcome.html', {'author': author})
        except ObjectDoesNotExist:
            author = Author(username=request.user.username, name=request.user.username)
            author.save()
            return render(request, 'welcome.html', {'message': 'Thanks for joining.  You can now create worlds.'})
    else:
        return render(request, 'welcome.html',)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

