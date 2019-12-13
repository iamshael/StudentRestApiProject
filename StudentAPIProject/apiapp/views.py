from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from apiapp.serializers import StudentSerializer
from apiapp.models import Student


# Create your views here.
def homeview(request):
    return HttpResponse("<h1>Hello Shailesh....</h1>")


@api_view(['GET','POST',])
def studentview(request):
    if request.method=="GET":
        stud = Student.objects.all()
        serializer = StudentSerializer(stud,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
