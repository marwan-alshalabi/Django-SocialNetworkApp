from django.contrib import admin
from django.urls import path , include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
 path('',login_page,name='login'),
 path('signup/' , SignupView.as_view(),name='signup'),
 path('logout/',logout_user,name='logout'),
 path('profile/',Profile.as_view(),name='profile'),
 path('account-settings/',AccountSettingsView.as_view(),name='account-settings'),
 path('new-post/',CreatePost.as_view(),name='new-post'),
 path('user/<str:username>/',FriendProfile.as_view(),name='friend-profile'),
 path('search/',SearchResulte.as_view(),name='search'),
 path('follow/<int:id>/',follow_user,name='follow-user'),
 path('unfollow/<int:id>/',unfollow_user,name='unfollow-user'),
 path('home/',HomePage.as_view(),name='home-page'),
 path('edit-post/<int:pk>/',EditPost.as_view(),name='edit-post'),
 path('delete-post/<int:pk>/',DeletePost.as_view()),



path('summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)