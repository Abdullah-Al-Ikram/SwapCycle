from django.shortcuts import render, get_object_or_404

from products.models import Product, Category


# Create your views here.
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    free_items = Product.objects.filter(price=0)
    return render(request, 'front/index.html', {'categories': categories, 'products': products, 'free_items': free_items})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'front/product-details.html', {'product': product})