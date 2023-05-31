from django.db import models
from tkinter import CASCADE

# Create your models here.

class Genre(models.Model):
    name = models.TextField()

class Tmdb(models.Model):
    genre_ids = models.ManyToManyField(Genre, related_name='tmdbs')
    title = models.TextField()
    overview = models.TextField()
    poster_path = models.TextField()
    vote_average = models.IntegerField()
    vote_count = models.IntegerField()
    release_date = models.DateField()
    

class Kobis(models.Model):
    order = models.IntegerField()
    name = models.TextField()
    open_data = models.TextField()
    average = models.FloatField()
    sales = models.TextField()
    sales_per = models.TextField()
    sales_variation = models.TextField()
    sales_total = models.TextField()
    spectators = models.TextField()
    spectators_variation = models.TextField()
    spectators_total = models.TextField()
    screen = models.TextField()
    screen_time = models.TextField()
    overview = models.TextField()


class Detail(models.Model):
    poster_path = models.TextField()
    movie_detail = models.TextField()

class Comment(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='child')
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
