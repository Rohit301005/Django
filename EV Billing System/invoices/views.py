from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is Home Page")

def about(request):
    return HttpResponse("This is about Page")

def show_invoice(request):
    data = {
        "customer_name": "Rohit Kumar Rawat",
        "invoice_total": 15000,
    }

    return render(request, "cust_name.html", data)


