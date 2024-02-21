from django.contrib import admin
from django.urls import path ,include
from .views import *

urlpatterns = [
    path('',login_page,name='login'),
    path ('signup/', SignUpView.as_view(),name='signup'),  
    path('profile/',profile, name='profile'),
] 