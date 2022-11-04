from django.contrib import admin
from .models import Artiste, Song,Lyric

# Register your models here.
class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Artiste)
admin.site.register(Song, SongAdmin)
admin.site.register(Lyric)
