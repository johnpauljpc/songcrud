from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    age = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length = 50)
    date_released = models.DateTimeField(auto_now_add = True)
    likes = models.CharField(max_length = 200)
    artist_id = models.ForeignKey(Artiste, on_delete = models.CASCADE) 

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)




'''
Model: Artiste, Song, Lyric
Attributes for “Artiste” : first_name, last_name, age
Attributes for “Song” : title, date released, likes, artiste_id
Attributes for “Lyric”: content, song_id
'''