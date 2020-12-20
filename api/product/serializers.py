from rest_framework import serializers
from .models import ProductModel

class ProductSeriaizer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(allow_null=True, max_length=None, allow_empty_file=True, required=False)
    class Meta:
        model = ProductModel
        fields = ("id", "name", "description", "stock", "price", "image")