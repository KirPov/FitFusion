from django.shortcuts import render, redirect
from .forms import OrderForm, ProductsForm
from django.views import generic

from .models import Products


def order(request):
    error = ""
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма неверна"
    form = OrderForm()
    data = {
        'error': error,
        'form': form,
    }
    return render(request, 'main/order.html', data)


def home(request):
    return render(request, 'main/home.html')


def product_catalog(request):
    return render(request, 'main/product_catalog.html')


def faq(request):
    return render(request, 'main/faq.html')


def add(request):
    error = ""
    if request.method == "POST":
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')
        else:
            error = "Форма неверна"
    form = ProductsForm()

    data = {
        'error': error,
        'form': form,
    }
    return render(request, 'main/reg.html', data)

class ProductsView(generic.ListView):
    template_name = 'main/product_catalog.html'
    context_object_name = 'products_list'
    def get_queryset(self):
        return Products.objects.all()

