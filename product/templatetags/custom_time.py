from datetime import datetime
from product.models import Product
from django import template


register = template.Library()


@register.simple_tag
def copyright_year():
    return Product.objects.count()