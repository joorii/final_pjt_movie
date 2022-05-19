from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

User = settings.AUTH_USER_MODEL

class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    overview = models.TextField()
    poster_path = models.TextField()
    director = models.CharField(max_length=30)
    average_vote = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0.0)
    release_date = models.DateField(null=True)


class WatchedMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0.0)


class Question(models.Model):
    content = models.CharField(max_length=100)


class Value(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value_id = models.IntegerField()
    content = models.CharField(max_length=200)
    director = models.CharField(max_length=30, null=True)