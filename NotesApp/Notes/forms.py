from django import forms
from .models import NoteModel

class NotecCreate(forms.ModelForm):
    class Meta:
        model = NoteModel
        firlds = '__all__'