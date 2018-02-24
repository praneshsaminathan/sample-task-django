from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
from django.urls import reverse


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == "POST":
        import ipdb; ipdb.set_trace()
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            error_msg = 'Invalid Credentials! Please Try Again'
            return render(request, 'login.html', locals())
        else:
            auth_login(request, user)
            return HttpResponseRedirect("/home/")
    return render(request, 'login.html')


@login_required
def logout(request):
    auth_logout(request)
    request.session.flush()
    if request.GET.get('next'):
        return HttpResponseRedirect(request.GET['next'])
    return HttpResponseRedirect('/')