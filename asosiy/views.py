from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def hamma_todo(request):
    data={"todo":Kundalik.objects.all()}
    return render(request,"todo.html",data)