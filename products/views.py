from django.shortcuts import render
from django.http import Http404
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializers
from rest_framework import status


@api_view(['GET', 'POST'])
def blogCreateListView(request):
    if request.method == 'GET':
        model = Product.objects.all()
        serializer = ProductSerializers(model, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def blogDetailUpdate(request, pk):
    if request.method == 'GET':
        model = Product.objects.get(pk=pk)
        serializer = ProductSerializers(model)
        return Response(serializer.data)

    if request.method == 'PUT':
        model = Product.objects.get(pk=pk)
        serializer = ProductSerializers(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        model = Product.objects.get(pk=pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)