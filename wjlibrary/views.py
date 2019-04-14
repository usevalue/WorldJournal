from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import World, Author


def shelves(request):
    return browse(request, World.objects.order_by('author'))


def browse(request, worlds):
    return render(request, 'shelves.html', {'worlds': worlds})


def read(request, world_id):
    world = World.objects.get(pk=world_id)
    author = getAuthor(request)
    if author == world.author:
        if request.method == 'POST':
            d = request.POST.get('descrip')
            if d:
                world.description = d
            h = request.POST.get('hist')
            if h:
                world.history_overview = h
            p = request.POST.get('purp')
            if p:
                world.purpose = p
            world.save()
    return render(request, 'desk.html', {'world': world, 'author': author})


def draft(request):
    if request.user.is_authenticated:
        author = getAuthor(request)
        if author:
            if request.method == 'POST':
                title = request.POST.get('world-title')
                description = request.POST.get('world-description')
                history = request.POST.get('world-history')
                purpose = request.POST.get('world-purpose')
                newWorld = World(title=title, author=author, description=description, history_overview=history, purpose=purpose)
                newWorld.save()
            worlds = World.objects.filter(author=author)
            if worlds.count() < 3:
                return render(request, 'writing.html', {'author': author})
            else:
                return render(request, 'shelves.html',
                              {'message': 'No more than three worlds per author!', 'worlds': worlds})
        else:
            return redirect('/', {'message': 'Your author record could not be found.  If problem persists, contact management.'})
    else:
        return redirect('/library/', {'message': 'You have to log in to create a world.'})


def delete(request, world_id):
    if request.method == 'POST':
        World.objects.get(pk=world_id).delete()
        return redirect('/library/', {'message': 'World obliterated.'})
    else:
        return redirect('/library/')


def getAuthor(request):
    try:
        author = Author.objects.get(username=request.user.username)
        return author
    except ObjectDoesNotExist:
        return False
