from rest_framework import viewsets
from .serializers import ProductSeriaizer
from .models import ProductModel
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSeriaizer

