from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def hamma_todo(request):
    data={"todo":Kundalik.objects.all()}
    return render(request,"todo.html",data)
def kundalik_edit(request,son):
    if request.method=="POST":
        Kundalik.objects.filter(id=son).update(
            vaqti=request.POST.get("v"),
            izoh=request.POST.get("i"),
            maqsad=request.POST.get("m")

        )
        return redirect("/todo/")
    data={"todo":Kundalik.objects.get(id=son)}
    return render(request,"kundalik_edit.html",data)