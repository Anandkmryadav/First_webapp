import operator

from django.http import HttpResponse
from django.shortcuts import render
from . import counter


def home(request):
    return render(request, "index.html", {'key': "I am coming from Python code"})


def result(request):
    article = request.GET.get('article', '')  # Using get() to avoid KeyError
    var_dict, word_count = counter.count(article)
    return render(request, "result.html",
                  {'article': article, 'word_count': word_count, 'var_dict': var_dict})c