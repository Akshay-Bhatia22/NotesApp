from django.http.response import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Notes.serializers import NoteModelSerializer

from django.shortcuts import render, redirect
from .models import NoteModel, Notelist
from .forms import NoteCreate
from django.db.models.query import QuerySet 

# ----------------------------------------------API-----------------------------------------------------------------------------------------------------------------------
@csrf_exempt
def List_notes_all_create_api(request):
    if request.method == 'GET':
        notes = NoteModel.objects.all()
        serialized_notes = NoteModelSerializer(notes, many=True)
        return JsonResponse(serialized_notes.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serialized_notes = NoteModelSerializer(data)
        if serialized_notes.is_valid():
            serialized_notes.save()
            return JsonResponse(serialized_notes.data, status=201)
        return JsonResponse(serialized_notes.errors, status=400)

@csrf_exempt
def Note_detail_api(request, Notes_title):
    try:
        note = NoteModel.objects.get(title=Notes_title)
        print("passed")
    except NoteModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serialized_note = NoteModelSerializer(note)
        return JsonResponse(serialized_note.data)

    elif request.method == 'PUT':
        data_parsed = JSONParser().parse(request)
        serialized_note = NoteModelSerializer(NoteModel,data_parsed)
        if serialized_note.is_valid():
            serialized_note.save()
            return JsonResponse(serialized_note.data)
        return JsonResponse(serialized_note.errors, status=400)

    elif request.method == 'DELETE':
        note.delete()
        return HttpResponse(status=204)


# ----------------------------------------------API-----------------------------------------------------------------------------------------------------------------------


def index(request):
    # shows the most recent note created
    all_notes = NoteModel.objects.order_by('-created')
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

def collections(request):
    collection_all = NoteModel.objects.order_by('collection')
    return render(request, 'Notes/collections.html', {'collection_all':collection_all})