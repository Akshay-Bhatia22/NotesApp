from django.db import models
from datetime import datetime
from django.utils import timezone

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class NoteModel(models.Model):
    title = models.CharField(max_length=40)
    created = models.DateTimeField(default=datetime.now(tz=timezone.utc))
    desc = models.CharField(max_length=80,blank=True)
    note_img = models.ImageField(blank=True)
    fav = models.BooleanField(default=False)
    collection = models.CharField(max_length=30,blank=True)

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