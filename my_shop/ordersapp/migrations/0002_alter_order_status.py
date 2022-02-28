# Generated by Django 3.2.3 on 2022-02-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('CREATED', 'Создан'), ('IN_PROCESSING', 'В обработке'), ('WAITING_PAYMENT', 'ОЖИДАЕТ ОПЛАТЫ'), ('PAID', 'Оплачен'), ('READY', 'Готов к выдаче'), ('CANCELED', 'Отменен'), ('FINISHED', 'Выдан')], default='CREATED', max_length=20, verbose_name='Статус'),
        ),
    ]
