from django.db import models
from django.conf import settings
from mainapp.models import Product

# Create your models here.


class Order(models.Model):
    CREATED = 'CREATED'
    IN_PROCESSING = 'IN_PROCESSING'
    AWAITING_PAYMENT = 'WAITING_PAYMENT'
    PAID = 'PAID'
    READY = 'READY'
    CANCELED = 'CANCELED'
    FINISHED = 'FINISHED'

    ORDER_STATUS_CHOICES = (
        (CREATED, 'Создан'),
        (IN_PROCESSING, 'В обработке'),
        (AWAITING_PAYMENT, 'ОЖИДАЕТ ОПЛАТЫ'),
        (PAID, 'Оплачен'),
        (READY, 'Готов к выдаче'),
        (CANCELED, 'Отменен'),
        (FINISHED, 'Выдан'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    status = models.CharField(verbose_name="Статус", choices=ORDER_STATUS_CHOICES, max_length=20)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    def __str__(self):
        return f'Заказ {self.id}'

    def get_total_cost(self):
        return sum(item.cost for item in self.items.select_related('product'))


    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('-created',)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)

    @property
    def cost(self):
        return self.product.price * self.quantity