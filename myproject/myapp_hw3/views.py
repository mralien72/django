from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, User, Product
from .forms import ProductForm
from django.utils import timezone
import logging
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "myapp_hw3/index.html")


def all_product(request):
    logger.info('Index page accessed')
    products = list(Product.objects.all())
    return render(request, 'myapp_hw3/all_product.html', {'products': products})


def all_orders(request):
    logger.info('Index page accessed')
    orders = list(Order.objects.all())
    return render(request, 'myapp_hw3/all_orders.html', {'orders': orders})


def orders_by_days(request, user_id, days):
    days_html = days
    user = get_object_or_404(User, pk=user_id)
    start_date = timezone.now() - timezone.timedelta(days=days)
    orders_user = Order.objects.filter(customer=user, date_ordered__gte=start_date)

    order_products = {}
    for order in orders_user:
        for product in order.products.all():
            if product not in order_products:
                order_products[product] = order.date_ordered
            else:
                order_products[product] = max(order_products[product], order.date_ordered)

    order_products = sorted(order_products.items(), key=lambda x: x[1], reverse=True)

    return render(request, f'myapp_hw3/orders_by_days.html', {
        'user': user,
        'order_products': order_products,
        'days_html': days_html
        })


def product_cart(request):
    # product = get_object_or_404(Product, pk=product_id)
    # return render(request, 'myapp_hw3/product_cart.html', {'product': product})
    product_id = request.GET.get('product_id')
    if product_id:
        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'myapp_hw3/product_cart.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product(name=form.cleaned_data['name'],
                             price=form.cleaned_data['price'],
                             description=form.cleaned_data['description'],
                             image=form.cleaned_data['image'],
                             quantity_products=form.cleaned_data['quantity_products'],
                             date_created=form.cleaned_data['date_created'],
                            )
            fs = FileSystemStorage()
            fs.save(product.image.name, product.image)
            product.save()
            return render(request, 'myapp_hw3/product_cart.html', {'product': product})
    else:
        form = ProductForm()
    return render(request, 'myapp_hw3/product_create.html', {'form': form})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'myapp_hw3/product_cart.html', {'product': product})



