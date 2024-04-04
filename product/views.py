from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from product.models import Product, Category, Review
from product.forms import ProductForm, ReviewForm


def main_page_view(request):
    MOCK_DATA = [
        {
            'id': 1,
            'name': 'John',
            'age': 25
        },
        {
            'id': 2,
            'name': 'Jane',
            'age': 30
        },
        {
            'id': 3,
            'name': 'Bob',
            'age': 35
        }
    ]
    context = {'name': 'Adilet', 'mock_data': MOCK_DATA}
    if request.method == 'GET':
        return render(request, 'main.html', context=context)

def hello_view(request):
    return HttpResponse("Hello! Its my project")

def current_date_view(request):
    return HttpResponse('Current date is %s' % datetime.date.today())

def goodby_view(request):
    return HttpResponse("Goodby user!")

def product_list_view(request):
    products = Product.objects.all()
    # print(products)
    context = {'products': products}
    return render(request, 'product/product_list.html', context)

def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return HttpResponse("Page not found")
        context = {'product': product,
                   'form': ReviewForm()}
        return render(request, 'product/product_detail.html', context)
    elif request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            Review.objects.create(product_id=product_id, **form.cleaned_data)
            return redirect(f'/products/{product_id}/')
        return render(request, 'product/product_detail.html', {'form': form})


def category_list_view(request):
    categories = Category.objects.all()
    # print(products)
    context = {'categories': categories}
    return render(request, 'category/category_list.html', context)

def product_create_view(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product/product_create.html', {'form': form})

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        # form.add_error('description', 'The text must not have the word Python')
        if not form.is_valid():
            return render(request, 'product/product_create.html', {'form': form})

        title = form.cleaned_data.get('title')
        description = form.cleaned_data.get('description')
        price = form.cleaned_data.get('price')
        size = form.cleaned_data.get('size')
        image = form.cleaned_data.get('image')

        Product.objects.create(title=title,
                               description=description,
                               price=price,
                               size=size,
                               image=image
                               )

        return redirect('product_list')

