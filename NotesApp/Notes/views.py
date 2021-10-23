from django.shortcuts import render
from .models import NoteModel

def index(request):
    all_notes = NoteModel.objects.all()
    return render(request, 'Notes/index.html', {'all_notes':all_notes})