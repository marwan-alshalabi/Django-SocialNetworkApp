from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
 path('',login_page,name='login'),
 path('signup/' , SignupView.as_view(),name='signup'),
 path('logout/',logout_user,name='logout'),
 path('profile/',profile,name='profile'),
 path('account-settings/',AccountSettingsView.as_view(),name='account-settings'),

]
