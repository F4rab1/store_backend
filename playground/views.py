from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product
from store.models import OrderItem


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
    # query_set = Product.objects.filter(description__isnull=False)
    # query_set = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20))
    # query_set = Product.objects.filter(inventory=F('unit_price'))
    # query_set = Product.objects.order_by('unit_price', '-title').reverse()
    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')
    # query_set = Product.objects.all()[5:10]
    # query_set = OrderItem.objects.values('product_id', 'product__title').distinct().order_by('product__title')
    # query_set = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    # query_set = Product.objects.only('id', 'title')
    query_set = Product.objects.defer('description')

    return render(request, 'hello.html', { 'name': 'Farabi', 'products': list(query_set)})
