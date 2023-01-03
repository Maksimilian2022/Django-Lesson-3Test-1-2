import urllib
from django.shortcuts import render, redirect
from django.http import HttpResponse
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_sort = Phone.objects.order_by(request.GET['sort'])
    context = {"phone_objects": phone_sort}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)







