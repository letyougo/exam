from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Teacher,School
from django.http.response import HttpResponse,HttpResponseRedirect



def index(request):
    return HttpResponse('hello')


@login_required
def school(request):

    return render(request,'school_client/index.html')
    # return HttpResponse('hello world')


def login(request):

    if request.method == 'GET':
        return render(request, 'account/login.html')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect(request.POST.get('next','/'))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/school')

