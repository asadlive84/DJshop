from django.urls import path
from product.views import product_list, \
    create_product, \
    product_details,\
    product_list_json,\
    product_edit_view,\
    product_list_table

app_name = 'product'

urlpatterns = [
    path('', product_list, name="home"),
    path('table/', product_list_table, name="home_table"),
    path('create/', create_product, name='create_product'),
    path('<str:slug>-<int:pk>/', product_details, name="product_details"),
    path('edit/<str:slug>-<int:pk>/', product_edit_view, name="product_edit_view"),
    path('json/', product_list_json, name="product_list_json"),
]