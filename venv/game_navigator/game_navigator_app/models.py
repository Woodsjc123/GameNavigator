from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Platform(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre, related_name='games')
    release_date = models.DateField
    rating = models.FloatField
    platforms = models.ManyToManyField(Platform, related_name='games')

    def __str__(self):
        return self.title

    
class UserGameRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        unique_together = ('user', 'game')  # Ensure each user can rate a game only once

    def __str__(self):
        return f"{self.user.username} - {self.game.name} - Rating: {self.rating}"
