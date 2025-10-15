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


def categories_bootstrap(request) :
    categories = Category.objects.all ()
    return render ( request, 'categories_bootstrap.html', {'categories' : categories} )


def products_bootstrap(request):
    products = Product.objects.all ()
    return render ( request, 'products_bootstrap.html', { 'products': products } )

def suppliers_bootstrap(request):
    suppliers = Supplier.objects.all()
    return render ( request, 'suppliers_bootstrap.html', { 'suppliers': suppliers } )