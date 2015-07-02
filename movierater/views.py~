from django.shortcuts import render
from django.utils import timezone
from .models import Movie, MovieUser, Vote
from .forms import AddMovieForm, VoteForm
from django.http import HttpResponseRedirect



def list_movies(request):
    movies = Movie.objects.all()
    return render(request, 'movierater/movie_list.html', {'movies': movies})


def add_movie(request):
    form = AddMovieForm()
    return render(request, 'movierater/add_movie.html', {'form': form})

def submit_movie(request):
    if request.method == "POST":
        form = AddMovieForm(request.POST)
        # import ipdb; ipdb.set_trace()
        if form.is_valid():
            data = form.cleaned_data
            if 'www' not in data['poster']:
                data['poster'] = None
            Movie.objects.create(
                title=data['title'],
                launch_date=data['launch_date'],
                imdb_link=data['imdb_link'],
                poster=data['poster'],
            )
            return HttpResponseRedirect("/")

    return HttpResponseRedirect("/add_movie/")
    # form = AddMovieForm(request.POST)
    # import ipdb; ipdb.set_trace()
    # print(form.is_valid())
    # return HttpResponseRedirect("/add_movie/")

def vote_movie(request, **kwargs):    
    form = VoteForm()
    movie = Movie.objects.get(id=kwargs['movie_id'])
    return render(request, 'movierater/vote_movie.html', {'form': form, 'movie': movie})

def submit_vote(request, **kwargs):
    if request.method == "POST":
        form = VoteForm(request.POST)
        # import ipdb; ipdb.set_trace()
        if form.is_valid():
            # if not form.has_changed():
            #     return HttpResponseRedirect("/vote_movie/" + kwargs['movie_id'])
            data = form.cleaned_data
            name = ''
            for tok in data['user_name'].split():
                name = name + tok
            name = name.lower()
            user, created = MovieUser.objects.get_or_create(name=name)
            movie = Movie.objects.get(id=kwargs['movie_id'])
            vote, created = Vote.objects.get_or_create(user=user, movie=movie)
            vote.grade = data['rate']
            vote.save()
            return HttpResponseRedirect("/")

    return HttpResponseRedirect("/")