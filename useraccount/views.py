from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from django.core import serializers

# # Create your views here.

@api_view(('GET',))
def all_user(request):
    
    users = User.objects.all().values()    
    return Response(users)


@api_view(('GET',))
def specific_user(request, pk):
    
    users = User.objects.get(id=pk)
    response = {
        "username" : users.username,
        'email' : users.email
    }
    return Response(response)
