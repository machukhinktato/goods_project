from django.shortcuts import render


def index(request):
    context = {
        'greetings': 'hello',
        'phrase': 'mike was there'
    }
    return render(request, 'index.html', context)