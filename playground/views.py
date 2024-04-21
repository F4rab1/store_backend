from django.shortcuts import render
from django.db.models import Q, F, Func, Value, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Order, Collection, Customer
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
    # query_set = Product.objects.defer('description')
    # query_set = Product.objects.select_related('collection').all()
    # query_set = Product.objects.prefetch_related('promotions').all()
    # query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # result = Product.objects.filter(collection_id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))
    # query_set = Product.objects.annotate(discounted_price=F('unit_price') * 0.9)
    # query_set = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )
    # query_set = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name')
    # )
    # query_set = Customer.objects.annotate(
    #     orders=Count('order')
    # )
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.9, output_field=DecimalField())
    # query_set = Product.objects.annotate(discounted_price=discounted_price)
    # query_set = Customer.objects.annotate(last_order_id=Max('order__id'))
    # query_set = Product. objects.all()
    # list (query_set)
    # query_set [0]
    # collection = Collection()
    # collection.title = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # collection.save()
    collection = Collection.objects.create(title='Video Games', featured_product=Product.objects.get(pk=1))
    collection.save()

    return render(request, 'hello.html', { 'name': 'Farabi' })
