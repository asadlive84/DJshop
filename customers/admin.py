from django.contrib import admin
from customers.models import Customer, CustomerBilling, CustomerOrder


admin.site.register(Customer)
admin.site.register(CustomerBilling)
admin.site.register(CustomerOrder)
