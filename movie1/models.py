
from django.db import models


class Movie(models.Model):
    actor = models.CharField(max_length=50)
    actor_movie = models.CharField(max_length=100)
    genre_movie = models.CharField(max_length=50)
    movie_logo = models.CharField(max_length=10000)

    def __str__(self):
        return self.actor + '~*~*~*~*~*~' + self.actor_movie


class Song(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=40)
    song_name = models.CharField(max_length=50)
