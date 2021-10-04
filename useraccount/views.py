from allauth.account.models import EmailAddress
from rest_framework.response import Response
from rest_framework.decorators import api_view

# # Create your views here.

@api_view(('GET',))
def all_user(request):
    
    users = EmailAddress.objects.all().values()
    return Response(users)
