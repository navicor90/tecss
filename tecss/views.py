from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm

def customers(request):
    latest_customers = Customer.objects.order_by('-businessId')[:5]
    output = ', '.join(c.fullname for c in latest_customers)
    return HttpResponse(output)

def newCustomer(request):
    print("hola campeon")
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('/thanks/')
    else:
        form = CustomerForm()
    return render(request,'tecss/customer.html',{'form':form})

def customerDetail(request, pk):
    cust_id = pk
    return HttpResponse("You're looking detail for cust id : %s" % cust_id)

def customerItems(request, cust_id):
    cust_id = pk
    return HttpResponse("You're looking items for cust id : %s" % cust_id)

