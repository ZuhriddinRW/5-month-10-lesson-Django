from django.urls import path
from . import views

urlpatterns = [
    path ( '', views.index, name='index' ),
    path ( 'categories_bootstrap/', views.categories_bootstrap, name='categories_bootstrap' ),
    path ( 'products_bootstrap/', views.products_bootstrap, name='products_bootstrap' ),
    path ( 'suppliers_bootstrap/', views.suppliers_bootstrap, name='suppliers_bootstrap' )
]