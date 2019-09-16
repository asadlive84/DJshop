from django.shortcuts import render
from customers.models import Customer
from customers.forms import CustomerModelForm
from django.contrib import messages


def customerhomepage(request):
    customers = Customer.objects.all().order_by('-created_at')
    context = {
        'customers': customers,
    }
    return render(request, 'customers/customer_list.html', context)


def create_new_customer(request):
    if request.method == 'POST':
        customers = CustomerModelForm(request.POST or None)

        if customers.is_valid():
            customers.save(commit=False)
            customers.user = request.user
            customers.save()
            messages.success(request, "Customer Created Successfully!")
        else:
            messages.warning(request, "Customer didn't create")

    else:
        customers = CustomerModelForm()

    return render(request, 'customers/create_customer.html', {'forms': customers})
