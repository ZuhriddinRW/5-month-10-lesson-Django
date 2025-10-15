from django.shortcuts import render
from .models import *


def index(request) :
    categories = Category.objects.all ()
    products = Product.objects.all ()
    context = {
        'categories' : categories,
        'products' : products,
    }
    return render ( request, 'index.html', context )


def categories(request):
    categories = Category.objects.all()
    return render( request, 'categories.html', { 'categories': categories } )


def categories_with_id(request, category_id) :
    categories = Category.objects.filter (category_id=category_id)
    return render ( request, 'categories.html', {'categories' : categories} )


def products_bootstrap(request):
    products = Product.objects.all ()
    return render ( request, 'products.html', { 'products': products } )


def suppliers_bootstrap(request):
    suppliers = Supplier.objects.all()
    return render ( request, 'suppliers.html', { 'suppliers': suppliers } )