from django.db import models


class Goods_Items(models.Model):
    name = models.CharField(verbose_name='товары', max_length=64, blank=True, unique=True)
    price = models.CharField(verbose_name='цена', max_length=64, blank=True)