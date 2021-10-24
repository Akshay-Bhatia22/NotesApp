from django.db import models
from datetime import datetime


class NoteModel(models.Model):
    title = models.CharField(max_length=40)
    created = models.DateTimeField(default=datetime.now)
    desc = models.CharField(max_length=80,blank=True)
    note_img = models.ImageField(blank=True)
    fav = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    def is_fav(self):
        if self.fav==True:
            return "Favourite"
        else:
            return ""

class Notelist(models.Model):
    link = models.ForeignKey(NoteModel, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    image = models.CharField(max_length=80)

    def __str__(self):
        return str(self.item)