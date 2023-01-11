from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    phone=Phone.objects.all()
    return redirect('catalog')


def show_catalog(request):
    phone = Phone.objects.order_by('name')
    phone = Phone.objects.order_by('price')
    phone = Phone.objects.order_by('-price')

    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
