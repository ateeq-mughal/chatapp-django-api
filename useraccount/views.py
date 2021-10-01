# from django.shortcuts import render
# from rest_framework.views import APIView


# # Create your views here.


# class AllUserView(models.Model):

#     def get(self, request):
        
#         query_set = User.objects.all()
#         print("HELLLOOO", query_set)

#         serializer = UserSerializer(query_set)
#         print("DEKHOOOOOOOOOOO", serializer.data)


#         return Response(serializer.data)