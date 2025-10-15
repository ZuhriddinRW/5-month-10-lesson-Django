from django.urls import path
from . import views

urlpatterns = [
    path ( '', views.index, name='index' ),
    path ( 'categories', views.categories, name='categories' ),
    path ( 'categories/<int:category_id>/', views.categories_with_id ),
    path ( 'products', views.products_bootstrap, name='products' ),
    path ( 'suppliers', views.suppliers_bootstrap, name='suppliers' )
]