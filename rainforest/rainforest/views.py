from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rainforest.models import Product


def products_page(request):
    products = Product.objects.all()
    context = {'products': products}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def root(request):
    return HttpResponseRedirect('products')


def product_details(request, id):
    product = Product.objects.get(pk=id)
    context = {'product': product}
    response = render(request, 'product_details.html', context)
    return HttpResponse(response)