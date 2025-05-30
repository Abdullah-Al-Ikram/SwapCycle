from django.contrib import messages
from django.db.models import OuterRef, Subquery
from django.shortcuts import redirect,render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Category, Product, PickupPoint, Order, Subscription
from .forms import CategoryForm, ProductForm, PickupPointForm, OrderForm, SubscribeForm
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q

def home(request):
    subs_form = SubscribeForm()
    if request.method == 'POST':
        subs_form = SubscribeForm(request.POST)
        if subs_form.is_valid():
            subs_form.save()
            messages.success(request, "Subscribed successfully!")
            return redirect('home')
    categories = Category.objects.all()
    products = Product.objects.all()
    free_items = Product.objects.filter(price=0)
    orders = Order.objects.select_related('product').all().order_by('-created_at')
    return render(request, 'front/index.html', {'categories': categories, 'products': products, 'free_items': free_items, 'orders': orders, 'subs_form': subs_form})
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'front/product-details.html', {'product': product})
def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, is_active=True)
    free_items = products.filter(price=0)
    return render(request, 'front/category_product.html', {'products': products, 'free_items': free_items, 'category': category, })
@login_required
def dashboard(request):
    orders = Order.objects.select_related('product').all().order_by('-created_at')
    current_user = request.user
    return render(request, 'back/dashboard.html', {
        'orders': orders,
        'current_user': current_user
    })

@login_required
def product_list(request):
    user = request.user
    if user.role == 'admin':
        products = Product.objects.all()
    elif user.role == 'seller':
        products = Product.objects.filter(user=user)
    else:
        products = Product.objects.none()  # or handle differently
    return render(request, 'back/product_list.html', {'products': products})
@login_required
def order_list(request):
    if request.user.role == 'admin':
        orders = Order.objects.all().order_by('-created_at')
    else:
        orders = Order.objects.filter(user=request.user).order_by('-created_at')  # Others see their own
    return render(request, 'back/order_list.html', {'orders': orders})

@login_required
def pickup_list(request):
    pickups = PickupPoint.objects.all()
    return render(request, 'back/pickup_list.html', {'pickups': pickups})
@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'back/category_list.html', {'categories': categories})
@login_required
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.posted_by = request.user
        product.save()
        return redirect('product-list')
    return render(request, 'back/product_form.html', {'form': form})
@login_required
def pickup_create(request):
    form = PickupPointForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pickup-list')
    return render(request, 'back/pickup_form.html', {'form': form})
@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryForm()
    return render(request, 'back/category_form.html', {'form': form})
@login_required
def order_create(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('order-list')
    return render(request, 'back/order_form.html', {'form': form})
@login_required
def place_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.user = request.user
            order.save()
            return redirect('order-list')
    else:
        form = OrderForm()
    return render(request, 'back/order_form.html', {'form': form, 'product': product})
@login_required
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Only admin users can access this page
    if not request.user.is_staff and not request.user.is_superuser and request.user.role != 'admin':
        messages.error(request, "You do not have permission to update order status.")
        return redirect('order-list')

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES):
            order.delivery_status = new_status
            order.save()
            messages.success(request, "Order status updated.")
            return redirect('order-list')
        else:
            messages.error(request, "Invalid status selected.")

    return render(request, 'back/delivery_status.html', {'order': order})
@login_required
def sells_page(request):
    if request.user.role != 'seller':
        messages.error(request, "Only sellers can view this page.")
        return redirect('dashboard')
    sells = Order.objects.select_related('product').filter(product__user=request.user).order_by('-created_at')
    return render(request, 'back/sells_list.html', {'sells': sells})
@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product-list')
    return render(request, 'back/up_product_form.html', {'form': form})

def product_search(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query),
        is_active=True
    ) if query else []

    return render(request, 'front/product_search.html', {
        'query': query,
        'results': results
    })

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect(reverse('product-list'))

@login_required
def subscription_list(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'back/subscribe.html', {'subscriptions': subscriptions})


