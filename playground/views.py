from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    # query_set = Product.objects.all()
    # query_set.filter().filter().order_by()
    # query_set = Product.objects.get()
    # query_set = Product.objects.filter()
    # try:
    #     product = Product.objects.get(id=0) 
    # except ObjectDoesNotExist:
    #     pass
    exists = Product.objects.filter(pk=0).exists()
    
    return render(request, 'hello.html', { 'name': 'Farabi'})
