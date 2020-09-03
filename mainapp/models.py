from django.db import models


class GoodsItems(models.Model):
    KG = 'KG'
    TBD = 'TBD'

    UNIT = (
        (KG, 'кг'),
        (TBD, 'требует уточнения'),
    )

    name = models.CharField(verbose_name='товар', max_length=64, blank=True, unique=True)
    price = models.CharField(verbose_name='цена', max_length=64, blank=True)
    date = models.DateField(verbose_name='дата прибытия', auto_now_add=True)
    shipper = models.CharField(verbose_name='поставщик', max_length=64, blank=True)
    quantity = models.CharField(verbose_name='количество', max_length=10, blank=True)
    unit = models.CharField(verbose_name='единица измерения', max_length=20, choices=UNIT, default=TBD)
