from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from products.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'home.html', context)

def help(request):
    return render(request, 'help.html')