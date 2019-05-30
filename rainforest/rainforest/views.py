from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from rainforest.models import Product

def root(request):
    return HttpResponseRedirect('products')

def products_page(request):
    return render(request, 'index.html', {
        'products': Product.objects.all(),
        'title':    "Hello world"
    })

def product_details(request, id):
    # product = Product.objects.get(pk=id)
    # context = {'product': product}
    # response = render(request, 'product_details.html', context)
    # return HttpResponse(response)

    # 👆 Same As Above
    return render(request, 'product_details.html',  {
        'product': Product.objects.get(pk=id)
    })