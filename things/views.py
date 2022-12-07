from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #response = HttpResponse("Welcome to Things")
    return render(request, 'home.html')
