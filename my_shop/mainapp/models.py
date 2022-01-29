from distutils.command.upload import upload
from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=50)
    description = models.TextField(verbose_name="описание", blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name="имя", max_length=50)
    price = models.DecimalField(
        verbose_name="цена", decimal_places=2, max_digits=7, default=0
    )
    color = models.PositiveIntegerField(verbose_name="цвет", default=0x000000)
    description = models.TextField(verbose_name="описание", blank=True)
    image = models.ImageField(verbose_name="картинка", blank=True, upload_to="products")
    quantity = models.PositiveIntegerField(verbose_name="количество", default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
