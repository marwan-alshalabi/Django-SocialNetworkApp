from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView , UpdateView
from .models import User
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.utils.decorators import method_decorator
# Create your views here.


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('profile')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('profile')
        return super(SignupView,self).get(*args,**kwargs)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == "GET":
            return render(request,'login.html')
        elif request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('profile')
            else:
                print("wrong username or password")
                return redirect('login')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')


@method_decorator(login_required(login_url='login'),name='dispatch')
class AccountSettingsView(UpdateView):
    model = User
    fields = ['first_name','last_name','profile_pic','bio']
    template_name = 'account_settings.html'
    success_url = '/profile/'

    def get_object(self, queryset=None):
        return self.request.user
