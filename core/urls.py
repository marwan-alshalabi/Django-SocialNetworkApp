from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
 path('',login_page,name='login'),
 path('signup/' , SignupView.as_view(),name='signup'),
 path('logout/',logout_user,name='logout'),
 path('profile/',Profile.as_view(),name='profile'),
 path('account-settings/',AccountSettingsView.as_view(),name='account-settings'),
 path('new-post/',CreatePost.as_view(),name='new-post'),

]
