from django.shortcuts import render, redirect
from django.contrib.postgres.search import SearchQuery, SearchVector
from .models import World, Author


def shelves(request):
    if request.method == 'POST':
        searchName = request.POST.get('world_author')
        query = SearchQuery(searchName)
        worlds = World.objects.annotate(search=SearchVector('authors')).filter(search=query)
    else:
        worlds = World.objects.all().order_by('title')
    return render(request, 'shelves.html', {'worlds': worlds})


def desk(request):
    if request.method == 'POST':
        return render(request, 'desk.html')


def desk(request, world_id):
    world = World.objects.get(pk=world_id)
    return render(request, 'desk.html', {'world': world})



