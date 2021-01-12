from django.db import models
from datetime import date
# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    banner = models.FileField(upload_to="Images")
    date = models.DateField(default= date.today)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    title = models.CharField(max_length= 30)
    mp3 = models.FileField(upload_to="Songs")
    artist = models.CharField(max_length= 30,default="Not Defined")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
