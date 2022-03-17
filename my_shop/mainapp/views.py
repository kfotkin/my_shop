from django.shortcuts import render, get_object_or_404
from django.http.request import HttpRequest
from .models import Product
from .models import ProductCategory
import random
from django.core.paginator import Paginator, EmptyPage


def index(request):
    products = Product.objects.all()

    return render(
        request,
        "mainapp/index.html",
        context={
            "title": "Главная",
             
            "products": products
            },
    )


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = ProductCategory.objects.all()
    return render(
        request,
        "mainapp/product.html",
        context={
            "title": "Продукты",
            
            "product": product,
            "categories": categories,
            "category": product.category,
        },
    )    


def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={
            "title": "Контакты",
            
        },
    )


def get_hot_product(queryset):
    return random.choice(queryset)


def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    hot_product = get_hot_product(products)
    return render(
        request,
        "mainapp/products.html",
        context={
            "title": "Продукты",
            
            "products": products.exclude(pk=hot_product.pk),
            "categories": categories,
            "hot_product": hot_product,
        },
    )


def category(request, category_id, page=1):
    categories = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, pk=category_id)
    products = Product.objects.filter(category=category)
    hot_product = get_hot_product(products)
    paginator = Paginator(products.exclude(pk=hot_product.pk), 3)
    try:
        products_page = paginator.page(page)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)

    return render(
        request,
        "mainapp/products.html",
        context={
            "title": "Продукты",
          
            "paginator": paginator,
            "page": products_page,
            "products": products_page,
            "categories": categories,
            "hot_product": get_hot_product(products),
            "category": category,
            "hot_product": get_hot_product(products),
        },
    )
