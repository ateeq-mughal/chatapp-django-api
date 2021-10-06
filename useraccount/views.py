from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from django.http import Http404
from django.core import serializers
from .models import Message
from rest_framework.views import APIView
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime


creds = credentials.Certificate("./useraccount/firebase-creds.json")

firebase_admin.initialize_app(creds, {
    'databaseURL': 'https://vue-chat-app-a0d64-default-rtdb.firebaseio.com/',
})

ref = db.reference('messeges')


# # Create your views here.

@api_view(('GET',))
def all_user(request):
    
    if request.user.is_authenticated:
        users = User.objects.all().values()    
        return Response(users)
    
    else:
        response = {
        "status" : "Unauthenticated"
        }
        return Response(response)



@api_view(('GET',))
def specific_user(request, pk):
    
    users = User.objects.get(id=pk)
    response = {
        "username" : users.username,
        'email' : users.email
    }
    return Response(response)

class SendMessage(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            try:
                user = User.objects.get(id=request.data["recieverId"])
                print(user)
            except:
                raise Http404("Reciever does not exist")

            msg = Message(
                message = request.data["message"],
                receieverId = request.data["recieverId"],
                room = request.data["room"],
                sendBy = request.user.id,#User.objects.get(id=request.user.id), # request.user.id,
                senderId = User.objects.get(id=request.user.id), # request.user.id,
                time = request.data["time"])
            msg.save()

            ref.push({
            "message" :  request.data["message"],
            "recieverId": request.data["recieverId"],
            "room": request.data["room"],
            "sendBy": request.user.id,
            "senderId": request.user.id,
            "time": request.data["time"]
            })
            

            return Response(request.data)
        
        else:
            response = {
        "status" : "Unauthenticated"
        }
        return Response(response)
