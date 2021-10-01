from django.urls import path, include
# import rest_auth.views import PasswordResetConfirmView



urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    # path('all-users/', ),

]