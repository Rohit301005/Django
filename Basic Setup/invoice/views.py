from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello,This is our Home Page in Django Projet")

def about(request):
    return HttpResponse("this is our about page ")

def contact(request):
    return HttpResponse("this is our contact page ")

# def show_invoice(request):
#     data = {
#         "customer_name" : "Rohit",
#         "Total amount" : 1000,
#     }
#     return render(request,"C:\\Users\\rawat\\OneDrive\\Desktop\\Django\\Basic Setup\\invoice\\Templates\\cust_name.html",data)

def contact(request):
    return HttpResponse("this is our contact page ")
