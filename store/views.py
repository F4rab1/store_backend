from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        return Response('ok')

@api_view()
def product_detail(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product, context={'request': request})
    return Response(serializer.data)

@api_view()
def collection_detail(request, pk):
    collection = Collection.objects.get(pk=pk)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)