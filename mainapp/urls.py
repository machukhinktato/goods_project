from django.urls import path
from .views import GoodsDetails

app_name = 'goods'

urlpatterns = [
    path('add/', GoodsDetails, name='goods_add_url'),
    # path('add/', GoodsDetails.as_view(), name='goods_add_url'),
]