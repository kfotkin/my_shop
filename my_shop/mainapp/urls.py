from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="main"),
    path("contact", views.contact, name="contact"),
    path("products", views.products, name="products"),
    path("products/<int:pk>", views.category, name="category"),
]
