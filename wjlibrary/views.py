from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import World, Author


def shelves(request):
    worlds = World.objects.all().order_by('author')
    return render(request, 'shelves.html', {'worlds': worlds})


def read(request, world_id):
    world = World.objects.get(pk=world_id)
    author = getAuthor(request)
    return render(request, 'desk.html', {'world': world, 'author': author})


def delete(request, world_id):
    if request.method == 'POST':
        World.objects.get(pk=world_id).delete()
        return redirect('/library/', {'message': 'World obliterated.'})
    else:
        return redirect('/library/')


def draft(request):
    if request.user.is_authenticated:
        author = getAuthor(request)
        if author:
            if request.method == 'POST':
                return press(request, author)
            if World.objects.filter(author=author).count() < 3:
                return render(request, 'writing.html', {'author': author})
            else:
                return redirect('/library/', {'message': 'No more than three worlds per author!'})
        else:
            return redirect('/', {'message': 'Weird error.  Redirecting you here is supposed to be a fix.'})
    else:
        return redirect('/library/', {'message': 'You have to log in to create a world.'})


def press(request, author):
    if request.method == 'POST':
        title = request.POST.get('world-title')
        description = request.POST.get('world-description')
        purpose = request.POST.get('world-purpose')
        newWorld = World(title=title, author=author, description=description, purpose=purpose)
        newWorld.save()
        return read(request, newWorld.pk)
    else:
        return redirect('/')


def getAuthor(request):
    try:
        author = Author.objects.get(username=request.user.username)
        return author
    except ObjectDoesNotExist:
        return False
