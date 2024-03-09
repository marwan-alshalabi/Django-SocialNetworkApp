from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
