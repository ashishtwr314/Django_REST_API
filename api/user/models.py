from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True )

    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)

    session_token = models.CharField(max_length=10, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
