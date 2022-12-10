from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Profile created successfully' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'signup.html', context)


def loginPage(request):
    if 'username' in request.session:
        return redirect('home')
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session['username']=username
                
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,'Username OR password is incorrect')
        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    if 'username' in request.session:
        request.session.flush()
    logout(request)
    return redirect('login')  
 
@login_required(login_url='login') 
@never_cache
def index(request):
    if 'username' in request.session:
        dict_docs = {
            'posts': Post.objects.all()
        }
        return render(request, 'home.html', dict_docs)
    return redirect('login')

@login_required(login_url='login') 
@never_cache
def about(request):
    
     return HttpResponse("Hello about")

@login_required(login_url='login') 
@never_cache
def contact(request):
    return HttpResponse("Hello cont")

@login_required(login_url='login') 
@never_cache
def post(request):
    return HttpResponse("Hello post")
