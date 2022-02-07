from django.shortcuts import render
from authapp.models import ShopUser


def user_create():
    pass


def users():
    users = ShopUser.objects.all().order_by('id')

    return render('', context={
        'title': 'Пользователи',
        'objects': users
    })



def user_update():
    pass


def user_delete():
    pass
