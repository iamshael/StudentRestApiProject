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


@api_view(['GET',])
def studentview(request):
    stud = Student.objects.all()
    if request.method=="GET":
        serializer = StudentSerializer(stud,many=True)
        return Response(serializer.data)
