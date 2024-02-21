from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login


class  SignUpView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'signup.html'
    
    def form_valid(self, form):
        user = form.save()
        return redirect('profile')


def login_page(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('profile')
        else:
            print("worng username or password")
            return redirect('login')




@login_required
def profile(reqeust):
    return HttpResponse("<h1>only authenticateed users  can see  this page </h1>")