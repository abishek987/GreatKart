from django.shortcuts import get_object_or_404, render
from categorie.models import Categorie
from .models import Product



def store(request,categorie_slug = None):
    categories = None
    product = None
    if categorie_slug != None:
        categories = get_object_or_404(Categorie,slug = categorie_slug)
        product = Product.objects.filter(categorie = categories,is_available = True)
        product_count = product.count()
    else:
        product = Product.objects.all().filter(is_available = True)
        product_count = product.count()
    context = {
        'product':product,
        'product_count':product_count,
    }
    return render(request,'store.html',context)

def product_detail(request, categorie_slug, product_slug):
    try:
        single_product = Product.objects.get(categorie__slug=categorie_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product':single_product,
    }
    return render(request,'product_detail.html',context)