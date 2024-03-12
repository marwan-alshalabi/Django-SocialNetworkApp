from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User , Post
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption'),
        widgets = {
            'caption': SummernoteWidget(),
            
        }