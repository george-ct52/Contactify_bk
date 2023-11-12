from django.contrib import admin
from django.urls import path
from .views import RegisterUser,Login, UserProfile,Logout, UserProfile

urlpatterns = [
    path("register", RegisterUser.as_view(),name='signup'),
    path("login", Login.as_view(),name='login'),
    path("user", UserProfile.as_view(),name='user'),
    path("logout", Logout.as_view(),name='logout')

   
]
