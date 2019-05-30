from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rainforest.models import Product

def products_page(request):
    products = Product.objects.all()
    context = {'products': products}
    response = render(request, 'index.html', context)
    return HttpResponse(response)   