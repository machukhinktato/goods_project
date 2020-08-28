from django.shortcuts import render
from django.views.generic import View
from .models import GoodsItems


class GoodsDetails():
    model = GoodsItems
    template = 'mainapp/index.html'

# def index(request):
#     data = GoodsItems.objects.all()
#     context = {
#         'greetings': 'hello',
#         'phrase': 'mike was there',
#         'data': data,
#     }
#     return render(request, 'index.html', context)
