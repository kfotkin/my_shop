from django.urls import path
from . import views

# app_name = "mainapp"

urlpatterns = [
    path("", views.index, name="main"),
    path("contact", views.contact, name="contact"),
    path("products", views.products, name="products"), 
    # path("products", views.products, name="all"), 
    path("products/<int:pk>", views.category, name="category"),
]

# urlpatterns = [
#     path("", views.products, name="all"),
#     path("<int:pk>", views.category, name="category"),
# ]
