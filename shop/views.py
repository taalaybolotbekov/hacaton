from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def index(request):
    return render(request, 'shop/index.html')

def shop(request):
    return render(request, 'shop/shop.html')

def contact(request):
    return render(request, 'shop/contact-us.html')

def product_details(request):
    return render(request, 'shop/product-details.html')

def product_affiliate(request):
    return render(request, 'shop/product-details-affiliate.html')

def product_group(request):
    return render(request, 'shop/product-details-group.html')

def product_variable(request):
    return render(request, 'shop/product-details-variable.html')

def cart(request):
    return render(request, 'shop/cart.html')