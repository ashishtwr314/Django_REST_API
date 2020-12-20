from django.shortcuts import render
from rest_framework import viewsets
from .models import CategoryModel
from .serializers import CategorySerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer