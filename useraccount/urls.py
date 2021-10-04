from django.urls import path, include
from .views import all_user
# from .views import AllUserView

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('all-users/', all_user),

]