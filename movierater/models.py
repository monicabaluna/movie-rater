from django.db import models
from django.utils import timezone


class Vote(models.Model):
    movie = models.ForeignKey('Movie', null=False, blank=False, related_name='votes')
    user = models.ForeignKey('MovieUser', null=False, blank=False, related_name='votes')
    grade = models.IntegerField(default=5)


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True, null=True, blank=False)
    launch_date = models.DateField(default=timezone.now, null=True, blank=False)
    imdb_link = models.URLField(max_length=100)
    poster = models.CharField(max_length=1000, default=None, null=True) #I'll add the link to the photo 

    def rating(self):
        rating = 0
        number_of_votes = 0
        for vote in self.votes.all():
            rating += vote.grade
            number_of_votes += 1
        if number_of_votes == 0:
            return 0

        return float(rating) / number_of_votes

    def __str__(self):
        return self.title


class MovieUser(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True, blank=False)
