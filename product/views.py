from django.core.serializers import json
from django.shortcuts import render, HttpResponse, get_object_or_404
from product.models import Product, Measure
from product.forms import ProductForms
from django.contrib import messages
from django.http import JsonResponse


def product_list(request):
    product_list = Product.objects.all().order_by('-created_at')

    context = {
        'product_list': product_list,
    }
    return render(request, 'product/product_list.html', context)


def product_list_table(request):
    product_list = Product.objects.all().order_by('-created_at')

    context = {
        'product_list': product_list,
    }
    return render(request, 'product/product_table.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForms(request.POST, request.FILES or None)

        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'Form is successfully submitted')
        else:
            messages.warning(request, 'Form is not submitted')
    form = ProductForms()

    return render(request, 'product/product_create.html', {'form': form, })


def product_details(request, slug, pk):
    product = get_object_or_404(Product, slug=slug, pk=pk)
    context = {
        'product': product,
    }
    return render(request, "product/product_details.html", context)


def product_list_json(request):
    product = Product.objects.all()
    product = [product]
    return JsonResponse({'product': product}, safe=False)


def product_edit_view(request, slug, pk):
    product = get_object_or_404(Product, slug=slug, pk=pk)
    qn=product.quantity
    if request.method == 'POST':
        form = ProductForms(request.POST, request.FILES or None, instance=product)
        print(request.FILES)
        if form.is_valid():
            pro = form.save()
            pro.user = request.user
            pro.quantity += qn
            pro.save()
            messages.success(request, 'Form is successfully Edited')
        else:
            messages.warning(request, 'Form is not submitted')
    form = ProductForms(instance=product)

    return render(request, 'product/product_edit_form.html', {'form': form})
