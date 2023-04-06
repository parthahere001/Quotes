from django.shortcuts import render
from rest_framework.views import APIView
from mainapp import serializers
from .models import QuoteModel
from .serializers import QuoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def backendfunction(request, pk = None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            obj = QuoteModel.objects.get(id=id)
            serializer = QuoteSerializer(obj)
            return Response(serializer.data)
        else:
            obj = QuoteModel.objects.all()
            serializer = QuoteSerializer(obj, many = True)
            return Response(serializer.data)
    if request.method == 'POST':
        serializer = QuoteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        id = pk
        obj = QuoteModel.objects.get(id = id)
        serializer = QuoteSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Uploaded'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'PATCH':
        id = pk
        obj = QuoteModel.objects.get(id = id)
        serializer = QuoteSerializer(obj, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        id = pk
        obj = QuoteModel.objects.get(id = id)
        if obj is not None:
            obj.delete()
            return Response({'msg':'Data Deleted'})
        else:
            return Response({'msg':'Data Does Not Exists'})

