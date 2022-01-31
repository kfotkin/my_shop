from django.shortcuts import render, get_object_or_404
from django.http.request import HttpRequest
from .models import Product
from .models import ProductCategory

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


def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={
            "title": "Контакты",
            "menu_links": MENU_LINKS,
        },
    )


def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    return render(
        request,
        "mainapp/products.html",
        context={
            "title": "Продукты",
            "menu_links": MENU_LINKS,
            "products": products,
            "categories": categories,
        },
    )


def category(request, pk):
    categories = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category=category)
    return render(
        request,
        "mainapp/products.html",
        context={
            "title": "Продукты",
            "menu_links": MENU_LINKS,
            "products": products,
            "categories": categories,
        },
    )
