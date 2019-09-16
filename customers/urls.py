from django.urls import path, re_path
from customers.views import customerhomepage, create_new_customer
app_name = 'customers'

urlpatterns = [
    path('', customerhomepage, name='customerhomepage'),
    path('c/', create_new_customer, name='customer_create'),

]