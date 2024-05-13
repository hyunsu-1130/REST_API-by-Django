from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


# ViewSet은 Django REST Framework에서 제공
# 일반적인 CRUD(Create, Read, Update, Delete) 작업을 추상화하여
# 개발자가 보다 쉽고 빠르게 API 구성
class ProductViewset(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
