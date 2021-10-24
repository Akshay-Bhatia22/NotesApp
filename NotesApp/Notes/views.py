from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import NoteModel, Notelist
from .forms import NoteCreate

def index(request):
    all_notes = NoteModel.objects.all()
    return render(request, 'Notes/index.html', {'all_notes':all_notes})

def create(request):
    create = NoteCreate()
    if request.method == 'POST':
        create = NoteCreate(request.POST, request.FILES)
        if create.is_valid():
            create.save()
            return redirect('Notes:index')
        else:
            return HttpResponse("worng")
    else:
        return render(request, 'Notes/create.html', {'create_form':create})

def update(request, Notes_title):
    try:
        update_note = NoteModel.objects.get(title = Notes_title)
    except:
        return redirect('Notes:index')
    update_form = NoteCreate(request.POST or None, instance = update_note)
    if update_form.is_valid():
        update_form.save()
        return redirect('Notes:index')
    return render(request, 'Notes/upload_form.html', {'upload_form':update_form})

def delete_note(request, Notes_title):
    try:
        delnote = NoteModel.objects.get(title = Notes_title)
    except:
        return redirect('Notes:index')
    delnote.delete()
    return redirect('Notes:index')

def detail(request, Notes_title):
    Note_detail = NoteModel.objects.get(title=Notes_title)
    # Note_detail_list = Notelist.objects.create(link=Note_detail,item="some items")
    return render(request, 'Notes/detail.html', {'detail_note':Note_detail})
