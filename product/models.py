from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify

PRODUCT_TYPE = (
    ('Cn', 'Consumable'),
    ('St', 'Storable'),
    ('Se', 'Service'),
)


class Measure(models.Model):
    name = models.CharField(max_length=50)
    ratio = models.FloatField()

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200,db_index=True)
    image = models.ImageField(upload_to='product/', default='product.png')
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    quantity = models.IntegerField(default=0)
    purchase_price = models.FloatField()
    sales_price = models.FloatField()
    product_type = models.CharField(max_length=2, choices=PRODUCT_TYPE)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product:product_details',  kwargs={'slug':self.slug, 'pk': self.id} )

    def total_purchase_price(self):
        return float(self.quantity)*self.purchase_price

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = f'{slugify(self.name)}'

        super().save(force_insert, force_update, using, update_fields)
