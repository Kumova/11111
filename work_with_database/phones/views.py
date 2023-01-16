from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    phone=Phone.objects.all()
    return redirect('catalog')


def show_catalog(request):
    phone = Phone.objects.order_by('phone__name','phone__price' )
 #   phone = Phone.objects.order_by('price')
    template = 'catalog.html'
    context = {
        'phone': phone,
#        'name': phone.name,
#        'price': phone.price,
#        'LTE': phone.lte_exists,
 #       'release_date': phone.release_date
    }
    return render(request, template, context)


def show_product(request, slug):
    phone=get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {
        'phone': phone,
 #       'name': phone.name,
 #       'price': phone.price,
  #      'LTE': phone.lte_exists,
  #      'release_date': phone.release_date
    }
    return render(request, template, context)
