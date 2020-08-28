from django.shortcuts import render
from .models import GoodsItems


def index(request):
    data = GoodsItems.objects.all()
    context = {
        'greetings': 'hello',
        'phrase': 'mike was there',
        'data': data,
    }
    return render(request, 'index.html', context)
