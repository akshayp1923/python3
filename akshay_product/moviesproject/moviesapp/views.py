from django.http import HttpResponse
from django.shortcuts import render, redirect
from  . models import Movies
from.forms import MoviesForm

# Create your views here.
def index(request):
    movie=Movies.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,"index.html",context)
def detail(request,movie_id):
    movie=Movies.objects.get(id=movie_id)
    return  render(request,"detail.html",{'movie':movie})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movie=Movies(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,"add.html")

def update(request,id):
    movies=Movies.objects.get(id=id)
    form=MoviesForm(request.POST or None,request.FILES,instance=movies)
    if form. is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'movies':movies})

def delete(request,id):
    if request.method=='POST':
        movies=Movies.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')

