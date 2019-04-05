from django.db import models


# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=25)
    artist_name = models.CharField(max_length=30)
    album_genre = models.CharField(max_length=10)
    album_cover = models.FileField()

    def_str_(self):
       return self.album_name

    def get absolute_url(self):
       return reverse('musical:index')


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=25)
    song_audio = models.FileField
