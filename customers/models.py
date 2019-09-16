from django.db import models
from django.conf import settings
from users.models import CustomUser
from django.urls import reverse
from product.models import Product


class Customer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, db_index=True)
    mobile_number = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customers:customer_details', args=[str(self.id)])


class CustomerOrder(models.Model):
    order_staff = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    name = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    products = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField(default=1)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.products.name} {self.quantity}"

    def get_total_price(self):
        return self.quantity * self.products.sales_price


class CustomerBilling(models.Model):
    order_staff = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    name = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(CustomerOrder)
    total_price = models.FloatField(null=True, blank=True)
    billing_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        total = 0
        for x in self.products.all():
            total += x.get_total_price()
        self.total_price = total
        super().save(force_insert, force_update, using, update_fields)





