from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from rainforest.models import Product


def root(request):
    return HttpResponseRedirect('products')

def products_page(request):
    return render(request, 'index.html', {
        'products': Product.objects.all()
    })

def product_details(request, id):
    return render(request, 'product_details.html',  {
        'product': Product.objects.get(pk=id)
    })

def product_new(request):
    pass