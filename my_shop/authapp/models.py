from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta

# Create your models here.


def get_activation_key_exp_date():
    return now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name="возраст", blank=True)
    avatar = models.ImageField(verbose_name="аватарка", blank=True, upload_to="users")
    phone = models.CharField(verbose_name="телефон", max_length=20, blank=True)
    city = models.CharField(verbose_name="город", max_length=20, blank=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=get_activation_key_exp_date)

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
