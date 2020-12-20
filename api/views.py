from django.http import JsonResponse


def APIHomeRoute(request):
    return JsonResponse({"info": "Django React BRO", "name": "Ashish"})
