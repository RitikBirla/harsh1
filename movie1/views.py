
from django.http import HttpResponse
from .models import Movie
from django .shortcuts import render


def index(request):
    rowd = request.POST.get('Row')
    columnd = request.POST.get('Column')
    submitbutton = request.POST.get('submit')
    context = {'rowd': rowd, 'cold': columnd, 'submitbutton': submitbutton}
    return render(request, 'movie1/index.html', context)


def detail(request, movie_id):
    return HttpResponse("<h1>Welcome in id : " + str(movie_id) + "</h1>")
