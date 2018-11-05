from django.db import models
#from django.core.urlresolver import reverse
from django.urls import reverse,resolvers
class Album(models.Model):
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField(max_length=500)
    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk})
    def __str__(self):
        return self.album_title +'-' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=100)
    song_title = models.CharField(max_length=200)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk})














