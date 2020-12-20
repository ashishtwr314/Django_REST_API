from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from .serializers import UserModelSerializer
from .models import UserModel
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
import strgen

@csrf_exempt

def signin(request):

    if not request.method == "POST":
        return JsonResponse({"error" : "NOT A POST METHODD"})
    
    email = request.POST["email"]
    password = request.POST["password"]

    usermodel = get_user_model()

    try:
        user = usermodel.objects.get(email=email)
        if user.check_password(password):
            user_dict = usermodel.objects.filter(email=email).values().first()
            user_dict.pop("password")

            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({"error": "Previous session exists"})
            
            token = strgen.StringGenerator("[\d\w]{10}").render()
            user.session_token  = token
            user.save()
            login(request, user)
            return JsonResponse({"token": token, "user": user_dict})

        else:
            return JsonResponse({"error": "Wrong Password"})
    except usermodel.DoesNotExist:
        return JsonResponse({"error": "Invaid Email"})


def signout(request, id):

    usermodel = get_user_model()

    try:
        user = usermodel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
        logout(request)
    except :
        return JsonResponse({"error": "Invalid User ID"})

    return JsonResponse({"success": "Logout Successfull"})
    

class UserViewSet(viewsets.ModelViewSet):

    permission_classes_by_action = {"create": [AllowAny]}

    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def get_permissions(self):
        
        try:
            return [permission() for permission in self.permission_classes_by_action]

        except KeyError:
            return [permission() for permission in self.permission_classes]
