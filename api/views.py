from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import NoteSerializer
from .models import Note
# Create your views here.
@api_view(['GET'])
def getRoutes(request):
      routes=[
            {
            "endpoint":"/notes",
            "type":"GET",
            "info":"get all the notes"
            },
            {
            "endpoint":"/notes/id",
            "type":"GET",
            "info":"get  the note with specific id",
            },
      ]
      return Response([routes])

@api_view(['GET'])
def getNotes(request):
      data=Note.objects.all()
      serializer=NoteSerializer(data,many=True)
      return Response(serializer.data)

@api_view(['GET'])
def getNote(request,pk):
      data=Note.objects.get(id=pk)
      serializer=NoteSerializer(data,many=False)
      return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request,pk):
      data=request.data
      note=Note.objects.get(id=pk)
      serializer=NoteSerializer(instance=note,data=data)
      if serializer.is_valid():
            serializer.save()
      return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request,pk):
      note=Note.objects.get(id=pk)
      note.delete()
      return Response('note was deleted');

@api_view(['POST'])
def addNote(request):
      data=request.data
      note=Note.objects.create(body=data['body'])
      serializer=NoteSerializer(note,many=False)
      if serializer.is_valid():
            serializer.save()
      return Response(serializer.data)