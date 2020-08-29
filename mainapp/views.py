from django.shortcuts import render, redirect
from django.views.generic import View
from .models import GoodsItems
from .forms import GoodsForm


class GoodsDetails(View):
    model_form = GoodsForm
    template = 'mainapp/index.html'

    def get(self, request):
        form = self.model_form
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(
            request,
            self.template,
            context={
                'form': bound_form
            }
        )
