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


def categories(request) :
    categories = Category.objects.all ()
    return render ( request, 'categories.html', {'categories' : categories} )


def categories_with_id(request, category_id) :
    categories = Category.objects.filter ( category_id=category_id )
    return render ( request, 'categories.html', {'categories' : categories} )


def products(request) :
    products = Product.objects.all ()
    categories = Category.objects.all ()
    context = {
        'products' : products,
        'categories' : categories
    }
    return render ( request, 'products.html', context )


def products_by_category(request, category_id) :
    products = Product.objects.filter ( category_id=category_id )
    categories = Category.objects.all ()
    return render ( request, 'products.html', {'products' : products, 'categories' : categories} )


def suppliers(request) :
    suppliers = Supplier.objects.all ()
    return render ( request, 'suppliers.html', {'suppliers' : suppliers} )