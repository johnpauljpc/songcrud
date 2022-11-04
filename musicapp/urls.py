from django.urls import path
from .views import ListSongView, ListArtisteView, FetchSong, Delete_Update_Song

urlpatterns = [
    path('', ListSongView.as_view(), name = 'songs'),
    path('artists/', ListArtisteView.as_view(), name= 'artists'),
    path('fetch/<slug:slug>/', FetchSong.as_view(), name='fetch-song'),
    path('delete-update/<slug:slug>/', Delete_Update_Song.as_view(), name='delete-song'),
]