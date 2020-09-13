from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import View
from django.template.loader import render_to_string
from .models import GoodsItems
from .forms import GoodsForm
from django.http import HttpResponseRedirect


class GoodsList(View):
    model = GoodsItems
    template = 'mainapp/index.html'

    @staticmethod
    def get(request):
        goods = model.objects.all()
        return render(
            request,
            template,
            context={
                model.__name__.lower(): goods,
                'goods': goods,
                'detail': True,
            }
        )


class GoodsDetails(View):
    model_form = GoodsForm()
    template = 'mainapp/goods_add.html'
    data = dict()

    @staticmethod
    def get(request):
        form = model_form
        return render(request, 'mainapp/index.html', context={'form': form})

    @staticmethod
    def post(request):
        if request.method == 'POST':
            form = GoodsForm(request.POST)
            if form.is_valid():
                form.save()
                data['correct'] = True
                goods = GoodsItems.objects.all()
                data['goods_html'] = render_to_string('mainapp/list.html', {'goods': goods})
            else:
                data['form_html'] = render_to_string('mainapp/goods_add.html', {'form': form}, request=request)

        else:
            data['correct'] = False
            data['form_html'] = render_to_string('mainapp/goods_add.html', {'form': model_form}, request=request)

        return JsonResponse(data)


# def GoodsList(request):
#     return render(request, 'mainapp/index.html', {'goods': GoodsItems.objects.all()})
#
#
# def GoodsDetails(request):
#     data = dict()
#     if request.method == 'POST':
#         form = GoodsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             data['correct'] = True
#             goods = GoodsItems.objects.all()
#             data['goods_html'] = render_to_string('mainapp/list.html', {'goods': goods})
#         else:
#             data['form_html'] = render_to_string('mainapp/goods_add.html', {'form': form}, request=request)
#
#     else:
#         data['correct'] = False
#         data['form_html'] = render_to_string('mainapp/goods_add.html', {'form': GoodsForm()}, request=request)
#
#     return JsonResponse(data)
