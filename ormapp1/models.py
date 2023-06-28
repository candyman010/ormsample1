from django.db import models

# Create your models here.
class Game(models.Model):
    Game_Name = models.CharField(max_length=50)
    Player_name = models.CharField(max_length=25)
    Game_type = models.CharField(max_length=50)
    Player_age = models.IntegerField()
    Player_city = models.CharField(max_length=50)