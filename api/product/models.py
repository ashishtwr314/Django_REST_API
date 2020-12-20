from django.db import models
from api.category.models import CategoryModel

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/", max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(CategoryModel,  on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.name
    


