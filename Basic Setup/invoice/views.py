from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello,This is our Home Page in Django Projet")

def about(request):
    return HttpResponse("this is our about page ")

def contact(request):
    return HttpResponse("this is our contact page ")

