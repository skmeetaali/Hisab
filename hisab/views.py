from django.shortcuts import render
from django.http import HttpResponse
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import  api_view

# Create your views here.
def hello(request):
    return HttpResponse("Hello Mitali")

@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "User registered successfully"}, status=201)
        return Response(serializer.errors, status=400)