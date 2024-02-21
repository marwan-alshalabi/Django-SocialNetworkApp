from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import SignupForm
# Create your views here.
def index(reqeust):
    return HttpResponse("<h1>Hello Django</h1>")


class  SignUpView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'signup.html'
    
    def form_valid(self, form):
        user = form.save()
        return redirect('profile')


def profile(reqeust):
    return HttpResponse("<h1>only authenticateed users  can see  this page </h1>")