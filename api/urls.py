from django.urls import path, include
from .views import APIHomeRoute

urlpatterns = [
    path('', APIHomeRoute),
    path("category/", include("api.category.urls")),
    path("product/", include("api.product.urls")),
    path("user/", include("api.user.urls"))
    
]
