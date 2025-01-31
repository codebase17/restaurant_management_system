from django.shortcuts import render, redirect
from .models import Product, Order
from .forms import OrderForm

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'product_list.html', {'products': products})

def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})

def order_success(request):
    return render(request, 'order_success.html')