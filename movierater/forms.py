from django import forms
from .models import Movie
from django.forms.extras.widgets import SelectDateWidget
import datetime


class AddMovieForm(forms.Form):

    # class Meta:
    #   model = Movie
    #   fields = ('title', 'launch_date', 'imdb_link', 'poster')
    title = forms.CharField()
    launch_date = forms.DateField(widget=SelectDateWidget, initial=datetime.date.today)
    imdb_link = forms.URLField(initial='http://')
    poster = forms.URLField(required=False)


class VoteForm(forms.Form):
    user_name = forms.CharField(initial="First_Name Last_Name")
    rate = forms.ChoiceField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (9001, "Over 9000")])
