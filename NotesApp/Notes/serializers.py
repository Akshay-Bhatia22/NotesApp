from rest_framework import serializers
from Notes.models import NoteModel, LANGUAGE_CHOICES, STYLE_CHOICES
from datetime import datetime

class NoteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteModel
        fields = ['title', 'created', 'desc', 'note_img', 'fav', 'collection']

    def create(self, validated_data):
        return NoteModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.created = validated_data.get('created', instance.created)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.note_img = validated_data.get('note_img', instance.note_img)
        instance.fav = validated_data.get('fav', instance.fav)
        instance.collection = validated_data.get('collection', instance.collection)
        instance.save()
        return instance