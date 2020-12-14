from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import *
# Create your views here.

def home(request):
    movies = Movies.objects.all()
    return render(request, "index.html",{'movies':movies})

def movie_detail(request, slug):
    movie = Movies.objects.filter(slug=slug).first()
    # print(movie)
    if movie == None:
        return render(request, '404.html')
    else:
        return render(request, 'movie_detail.html', {"movie":movie})

def search(request):
    try:
        if request.method == 'GET':
            query = request.GET["search"]
            movies = Movies.objects.filter(name__contains = query)
            return render (request, 'search.html', {'movies':movies})
        else:
            return render(request, '404.html')
        
    except:
        return render(request, '404.html')