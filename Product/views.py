from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Product
from .serializers import ProductSerializaer
from rest_framework.response import Response
# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    def get_home(request):
        return render(request,'home.html')
    def create(seft,request):
        serializer = ProductSerializaer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    def update(seft,request,pk=None):
        product = Product.objects.get(id=pk)
        serializaer = ProductSerializaer(instance=product,data=request.data)
        serializaer.is_valid(raise_exception=True)
        serializaer.save()
        return Response(serializaer.data,status=status.HTTP_202_ACCEPTED)
    def destroy(seft,request,pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response("success")

