from django.shortcuts import render, get_object_or_404
from django.http.request import HttpRequest
from .models import Product
from .models import ProductCategory
import random
from django.core.paginator import Paginator, EmptyPage

MENU_LINKS = [
    {"url": "main", "name": "домой"},
    {"url": "contact", "name": "контакты"},
    {"url": "products:all", "name": "продукты"},
]


def index(request):
    products = Product.objects.all()

    return render(
        request,
        "mainapp/index.html",
        context={
            "title": "Главная",
            "menu_links": MENU_LINKS, 
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
            "menu_links": MENU_LINKS,
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
            "menu_links": MENU_LINKS,
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
            "menu_links": MENU_LINKS,
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
            "menu_links": MENU_LINKS,
            "paginator": paginator,
            "page": products_page,
            "products": products_page,
            "categories": categories,
            "hot_product": get_hot_product(products),
            "category": category,
            "hot_product": get_hot_product(products),
        },
    )
