from django.db import models

# Create your models here.
class album(models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class song(models.Model):
    album = models.ForeignKey(album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=100)
    song_title = models.CharField(max_length=100)

    def __str__(self):
        return self.song_title + '.' + self.file_type
