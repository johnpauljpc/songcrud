from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Song(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField()
    date_released = models.CharField(max_length = 50, default=2016)
    likes = models.CharField(max_length = 200, default=0)
    artist_id = models.ForeignKey(Artiste, on_delete = models.CASCADE) 

    def __str__(self):
        return f'{self.title} - {self.artist_id}'

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)

    def __str__(self):
        return f'Lyrics - {self.song_id.title}'




'''
Model: Artiste, Song, Lyric
Attributes for “Artiste” : first_name, last_name, age
Attributes for “Song” : title, date released, likes, artiste_id
Attributes for “Lyric”: content, song_id
'''