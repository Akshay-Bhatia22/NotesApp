from django import forms
from .models import NoteModel

class NoteCreate(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = ['title', 'desc', 'fav', 'note_img']