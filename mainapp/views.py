from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import View
from django.template.loader import render_to_string
from .models import GoodsItems
from .forms import GoodsForm
from django.http import HttpResponseRedirect


# class GoodsList(View):
#     model = GoodsItems
#     template = 'index.html'
#
#     def get(self, request):
#         goods = self.model.objects.all()
#         return render(
#             request,
#             self.template,
#             context={
#                 self.model.__name__.lower(): goods,
#                 'goods': goods,
#                 'detail': True,
#             }
#         )
#
#
# class GoodsDetails(GoodsList, View):
#     model_form = GoodsForm
#     template = 'mainapp/goods_add.html'
#     data = {}
#
#     def get(self, request):
#         form = GoodsForm()
#         return render(request, self.template, context={'form': form})
#
#     def post(self, request):
#         if request.method == "POST":
#             form = self.model_form(request.POST)
#             if form.is_valid():
#                 form.save()
#                 data['form_is_valid'] = True
#                 goods = self.model.objects.all()
#                 data['goods_html'] = render_to_string(
#                     'mainapp/list.html', {'goods': goods})
#             else:
#                 data['form_html'] = render_to_string('mainapp/goods_add.html', {'form': form}, request=request)
#         else:
#             data['form_is_valid'] = False
#             data['form_html'] = render_to_string('mainapp/goods_add.html', {'form': self.model_form()}, request=request)
#
#         return JsonResponse(data)


                                        #     bound_form = self.model_form(request.POST)
                                        # if bound_form.is_valid():
                                        #     bound_form.save()
                                        #     return HttpResponseRedirect('/')
                                        # return render(
                                        #     request,
                                        #     self.template,
                                        #     context={
                                        #         'form': bound_form
                                        #     }
                                        # )

def GoodsList(request):
    return render(request, 'mainapp/index.html', {'goods': GoodsItems.objects.all()})


def GoodsDetails(request):
    data = dict()
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
        data['form_html'] = render_to_string('mainapp/goods_add.html', {'form': GoodsForm()}, request=request)

    return JsonResponse(data)

