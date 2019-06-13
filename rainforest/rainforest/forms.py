from django.forms import ModelForm
from rainforest.models import Product

class ProductForm(ModelForm):
    pass
    # classs Meta:
    # model = Product
    # fields = ['name', 'description', 'fields']


    # form = ProductForm()

