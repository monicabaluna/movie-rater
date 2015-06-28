from django.contrib import admin
from .models import Movie
from .models import Vote
from .models import MovieUser

admin.site.register(Movie)
admin.site.register(MovieUser)
admin.site.register(Vote)