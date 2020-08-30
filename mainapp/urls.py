from django.urls import path
from .views import GoodsDetail

urlpatterns = [
    path('', mainapp.goods_list),
]