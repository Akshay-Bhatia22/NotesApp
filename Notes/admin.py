from django.contrib import admin
from Notes.models import NoteModel, Notelist

# Register your models here.
admin.site.register(NoteModel)
admin.site.register(Notelist)
