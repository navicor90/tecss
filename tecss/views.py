from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm

def index(request):
    return render(request, 'tecss/index.html')

def newCustomer(request):
    print("hola campeon")
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tecss/customers') 
    else:
        form = CustomerForm()
    return render(request,'tecss/customer.html',{'form':form})

def customerDetail(request, pk):
    cust_id = pk
    return HttpResponse("You're looking detail for cust id : %s" % cust_id)

def customerItems(request, cust_id):
    cust_id = pk
    return HttpResponse("You're looking items for cust id : %s" % cust_id)

