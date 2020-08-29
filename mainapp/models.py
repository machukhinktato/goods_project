from django.db import models


class GoodsItems(models.Model):
    name = models.CharField(verbose_name='товары', max_length=64, blank=True)
    price = models.CharField(verbose_name='цена', max_length=64, blank=True)