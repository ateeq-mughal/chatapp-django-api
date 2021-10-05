from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):

    
    message = models.CharField(max_length=50000)
    receieverId = models.IntegerField(null=False)
    room = models.CharField(max_length=255, null=False)
    sendBy = models.IntegerField(null=True)
    senderId = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    time = models.BigIntegerField(null=False)

    # def __str__(self):
    #     return self.



