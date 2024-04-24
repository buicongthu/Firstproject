from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Product
from .serializers import ProductSerializaer
from .serializers import CompanySerializaer
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import action
from django.http import JsonResponse
# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    def get_home(request):
        return render(request,'home.html')
  
    def create(seft,request):
        serializer = ProductSerializaer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    def retrieve(seft,pk =None):
        product = Product.objects.get(id=pk)
        serializer = Product(product)
        return Response(serializer.data)
    @action(detail=False, methods=['post'])
    def add(seft,request):
        serializer = ProductSerializaer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    def findProductByCompany(request,company):
        try:
            product = Product.objects.get(name = company)
            return JsonResponse({'products':product})
        except:
           return JsonResponse({'error':'fail'}, status=404) 



class CompanyViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def add(seft,request):
        serializer = CompanySerializaer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


