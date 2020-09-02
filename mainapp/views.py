from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import GoodsItems
from .forms import GoodsForm
from django.http import HttpResponseRedirect


class GoodsList(View):
    model = GoodsItems
    template = 'index.html'

    def get(self, request):
        goods = self.model.objects.all()
        return render(
            request,
            self.template,
            context={
                self.model.__name__.lower(): goods,
                'goods': goods,
                'detail': True,
            }
        )


# def goods_list(request):
#     goods = GoodsItems.objects.all()
#     return render(request, 'index.html', context={'goods': goods})


class GoodsDetails(View):
    model_form = GoodsForm
    template = 'mainapp/goods_add.html'

    def get(self, request):
        form = self.model_form
        return render(request, self.template, context={'form': form})

    def post(self, request):
        if request.method == "POST":
            bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return HttpResponseRedirect('/')  # return render(request, self.template, context={'form': form})
        return render(
            request,
            self.template,
            context={
                'form': bound_form
            }
        )
