from django.shortcuts import render
from .models import Pizza, Product, Drink, Ingredients
from django.http import HttpResponse

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    print(products)
    return render(request, 'index.html', context)

def get_all_product(request, id_product):
    if id_product == 1:
        pizzas = Pizza.objects.all()
        products = Product.objects.all()
        current_product = Product.objects.get(pk=id_product)
        context = {'objects': pizzas, 'products': products, 'current_product': current_product}
        return render(request, 'product.html', context)


    elif id_product == 2:
        drinks =  Drink.objects.all()
        products = Product.objects.all()
        current_product = Product.objects.get(pk=id_product)
        context = {'objects': drinks, 'products': products, 'current_product': current_product}
        return render(request, 'product.html', context)

    else:
        return HttpResponse('Product not found')


