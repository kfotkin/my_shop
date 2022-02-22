from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


def get_activation_key_exp_date():
    return now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name="возраст", blank=True, default=18)
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

 
class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    )

    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE, related_name="profile")
    about = models.TextField(verbose_name="о себе", max_length=512, blank=True)
    gender = models.CharField(verbose_name="выбор пола", choices=GENDER_CHOICES, max_length=1)

@receiver(post_save, sender=ShopUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ShopUserProfile.objects.create(user=instance)
    else:
        instance.profile.save()
    
