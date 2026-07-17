from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is Home Page")


# def show_invoice(request):
#     data = {
#         "customer_name": "Rohit Kumar Rawat",
#         "invoice_total": 15000,
#     }

#     return render(request, "C:\\Users\\rawat\\OneDrive\\Desktop\\Django\\1-Templates\\invoices\\templates\\cust_name.html", data)


