from django.urls import path
from .views import GoodsDetails

urlpatterns = [
    path('', GoodsDetails.as_view(), name='goods_add_url'),
]