from django.shortcuts import render
from .models import Artiste, Song,Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
#API View to list all the songs in our database and all the artists
class ListSongView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

#API View to list all the artists in our database
class ListArtisteView(ListAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer


#API View to fetch a particular song
class FetchSong(RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'slug'

#API View to delete and update a particular song
class Delete_Update_Song(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'slug'
