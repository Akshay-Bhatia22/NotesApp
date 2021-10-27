from django.http.response import HttpResponse
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Notes.serializers import NoteModelSerializer

from django.shortcuts import render, redirect
from .models import NoteModel, Notelist
from .forms import NoteCreate
from django.db.models.query import QuerySet 

# ----------------------------------------------Function Based API-----------------------------------------------------------------------------------------------------------------------

# @api_view(['GET'])
# def List_notes_all_get_api(request, format=None):
#     if request.method == 'GET':
#         notes = NoteModel.objects.all()
#         serialized_notes = NoteModelSerializer(notes, many=True)
#         return Response(serialized_notes.data)

#     # elif request.method == 'POST':
#     #     serialized_notes = NoteModelSerializer(request.data)
#     #     if serialized_notes.is_valid():
#     #         serialized_notes.save()
#     #         return Response(serialized_notes.data, status=status.HTTP_201_CREATED)
#     #     return Response(serialized_notes.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Note_create_api(request):
    if request.method == 'POST':
        serialized_notes = NoteModelSerializer(data = request.data)
        if serialized_notes.is_valid():
            serialized_notes.save()
            return Response(serialized_notes.data, status=status.HTTP_201_CREATED)
        return Response(serialized_notes.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'PUT', 'DELETE'])
# def Note_detail_api(request, Notes_title, format=None):
#     try:
#         note = NoteModel.objects.get(title=Notes_title)
#         print("passed")
#     except NoteModel.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serialized_note = NoteModelSerializer(note)
#         return Response(serialized_note.data)

#     elif request.method == 'PUT':
#         # data_parsed = JSONParser().parse(request)
#         serialized_note = NoteModelSerializer(data = request.data)
#         if serialized_note.is_valid():
#             serialized_note.save()
#             return Response(serialized_note.data)
#         return Response(serialized_note.errors, status=400)

#     elif request.method == 'DELETE':
#         note.delete()
#         return HttpResponse(status=204)


# ----------------------------------------------Class Based API-----------------------------------------------------------------------------------------------------------------------
class List_notes_all_get_api(APIView):
    def get(self, request, format=None):
        notes = NoteModel.objects.all()
        serialized_notes = NoteModelSerializer(notes, many=True)
        return Response(serialized_notes.data)

    def post(self, request, format=None):
        serialized_notes = NoteModelSerializer(data = request.data)
        if serialized_notes.is_valid():
            serialized_notes.save()
            return Response(serialized_notes.data, status=status.HTTP_201_CREATED)
        return Response(serialized_notes.errors, status=status.HTTP_400_BAD_REQUEST)

class Note_detail_api(APIView):

    def get_object(self, Notes_title):
        try:
            print("hi")
            return NoteModel.objects.get(title=Notes_title)
        except NoteModel.DoesNotExist:
            raise Http404

    def put(self, request, Notes_title, format=None):
        note = self.get_object(Notes_title)
        serialized_note = NoteModelSerializer(note, data=request.data)
        if serialized_note.is_valid():
            serialized_note.save()
            return Response(serialized_note.data)
        return Response(serialized_note.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, Notes_title, format=None):
        note = self.get_object(Notes_title)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
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