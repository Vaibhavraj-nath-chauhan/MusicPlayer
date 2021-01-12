from django.shortcuts import render
from django.http import HttpResponse

def Albums(request):
    return render(request,"Home.html")

