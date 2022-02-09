from django.urls import path
from . import views

urlpatterns = [
<<<<<<< Updated upstream
    path("", views.index, name="main"),
    path("contact", views.contact, name="contact"),
    path("products", views.products, name="products"),
    path("products/<int:pk>", views.category, name="category"),
=======
    path("", views.products, name="all"),
    path("<int:category_id>", views.category, name="category"),
    path("product/<int:product_id>", views.product, name="product"),
>>>>>>> Stashed changes
]
