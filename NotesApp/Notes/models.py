from django.db import models

class NoteModel(models.Model):
    title = models.CharField(max_length=40)
    created = models.DateTimeField('date published')
    desc = models.CharField(max_length=80)
    fav = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

class Notelist(models.Model):
    link = models.ForeignKey(NoteModel, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    image = models.CharField(max_length=80)

    def __str__(self):
        return str(self.item)