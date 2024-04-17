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
    # exists = Product.objects.filter(pk=0).exists()
    # keyword argument = value
    # query_set = Product.objects.filter(unit_price=20)
    # query_set =Product.objects.filter(unit_price__range=(10,30)) unit_price__gt=20
    # query_set = Product.objects.filter(collection__id__lt=4)
    # query_set = Product.objects.filter(title__icontains="coffee")
    # query_set = Product.objects.filter(last_update__year=2023)
    query_set = Product.objects.filter(description__isnull=True)

    
    return render(request, 'hello.html', { 'name': 'Farabi', 'products': list(query_set)})
